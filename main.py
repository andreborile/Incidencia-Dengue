import sqlite3 as conector
import pandas as pd
import os
import sql_commands
from modelos import *

# inicia as variaveis de conexao e cursor
conexao = None
cursor = None

try:
    # inicia a conexao e cria o banco de dados
    conexao = conector.connect('database.db')
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # cria as tabelas no banco de dados
    cursor.execute(sql_commands.cria_tab_municipio)
    cursor.execute(sql_commands.cria_tab_populacao)
    cursor.execute(sql_commands.cria_tab_dengue)

    # incrementando os dados nas tabelas
    with open('src/dengue_sc_2018_2021.csv') as file:
        file.readline() # descarta o cabecalho
        for linha in file:
            id, municipio, casos_2018, casos_2019, casos_2020, casos_2021 = linha.strip().split(';')
        
            # cria objeto muncipio
            municipio = Municipio(id, municipio)
            cursor.execute(sql_commands.insert_municipio, vars(municipio))

            # cria objeto casos de dengue
            dengue_2018 = Dengue(id, 2018, casos_2018)
            dengue_2019 = Dengue(id, 2019, casos_2019)
            dengue_2020 = Dengue(id, 2020, casos_2020)
            dengue_2021 = Dengue(id, 2021, casos_2021)
            cursor.execute(sql_commands.insert_dengue, vars(dengue_2018))
            cursor.execute(sql_commands.insert_dengue, vars(dengue_2019))
            cursor.execute(sql_commands.insert_dengue, vars(dengue_2020))
            cursor.execute(sql_commands.insert_dengue, vars(dengue_2021))

    with open('src/pop_sc_2018_2021.csv') as file:
        file.readline() # descarta o cabecalho
        for linha in file:
            id, municipio, pop_2018, pop_2019, pop_2020, pop_2021 = linha.strip().split(';')

            # cria objeto populacao
            pop_2018 = Populacaco(id, 2018, pop_2018)
            pop_2019 = Populacaco(id, 2019, pop_2019)
            pop_2020 = Populacaco(id, 2020, pop_2020)
            pop_2021 = Populacaco(id, 2021, pop_2021)
            cursor.execute(sql_commands.insert_populacao, vars(pop_2018))
            cursor.execute(sql_commands.insert_populacao, vars(pop_2019))
            cursor.execute(sql_commands.insert_populacao, vars(pop_2020))
            cursor.execute(sql_commands.insert_populacao, vars(pop_2021))

    conexao.commit()
    
    # Intervalo de anos de 2018 a 2021
    for ano in range(2018, 2022):
        # Selecionando dados
        sql_select = '''SELECT Municipio.municipio, Dengue.casos, Populacao.populacao
                        FROM Municipio
                        JOIN Dengue ON Municipio.id = Dengue.id
                        JOIN Populacao ON Municipio.id = Populacao.id
                        WHERE Dengue.ano=:ano AND Populacao.ano=:ano'''

        params = {'ano': ano}
        resultado = pd.read_sql(sql=sql_select, con=conexao, params=params)
        
        resultado['incidencia'] = (100 * resultado['casos'] / resultado['populacao']).round(6)
        nome_arquivo = f'incidencia_{ano}.csv'
        resultado.to_csv(nome_arquivo, index=False, sep=';')

    conexao.commit()

except conector.DatabaseError as e:
    print("Erro no banco de dados", e)
finally:
    # fechamento de conexao e cursor
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()