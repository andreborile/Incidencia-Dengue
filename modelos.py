class Municipio():
    def __init__(self, id, municipio) -> None:
        self.id = id
        self.municipio = municipio

class Populacaco():
    def __init__(self, id, ano, populacao) -> None:
        self.id = id
        self.ano = ano
        self.populacao = populacao

class Dengue():
    def __init__(self, id, ano, casos) -> None:
        self.id = id
        self.ano = ano
        self.casos = casos