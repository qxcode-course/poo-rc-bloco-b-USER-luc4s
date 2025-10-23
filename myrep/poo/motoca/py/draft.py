class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    def getNome(self):
        return self._nome
    
    def getIdade(self):
        return self._idade
    
    def __str__(self):
        return f"{self._nome}:{self._idade}"
    
class Motoca:
    