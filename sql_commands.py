cria_tab_municipio = ''' CREATE TABLE IF NOT EXISTS Municipio (
    id INTEGER NOT NULL,
    municipio VARCHAR(32) NOT NULL,
    PRIMARY KEY (id)
);'''

insert_municipio = ''' INSERT OR IGNORE INTO Municipio
VALUES (:id, :municipio);'''

cria_tab_populacao = ''' CREATE TABLE IF NOT EXISTS Populacao (
    id INTEGER NOT NULL,
    ano INTEGER NOT NULL,
    populacao INTEGER NOT NULL,
    PRIMARY KEY (id, ano),
    FOREIGN KEY(id) REFERENCES Municipio(id)
);'''

insert_populacao = ''' INSERT OR IGNORE INTO Populacao
VALUES (:id, :ano, :populacao);'''

cria_tab_dengue = ''' CREATE TABLE IF NOT EXISTS Dengue (
    id INTEGER NOT NULL,
    ano INTEGER NOT NULL,
    casos INTEGER NOT NULL,
    PRIMARY KEY (id, ano),
    FOREIGN KEY(id) REFERENCES Municipio(id)
);'''

insert_dengue = ''' INSERT OR IGNORE INTO Dengue
VALUES (:id, :ano, :casos);'''