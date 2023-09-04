import sqlite3 as conector

# inicia as variaveis
conexao = None
cursor = None

try:
    # inicia a conexao e cria o banco de dados
    conexao = conector.connect('database.db')
except conector.DatabaseError as e:
    print("Erro no banco de dados", e)
finally:
    # fechamento de conexao e cursor
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()