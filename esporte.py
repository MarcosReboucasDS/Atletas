from abc import ABC
from typing import List
class Atleta(ABC): #CLASSE ABSTRATA, ONDE É APENAS UM MODELOS, NÃO SE FAZ ALGUMA ALTERAÇÃO ABSTRACT BASIC CLASS
    nome: str
    idade: int
    peso: float

    def __init__(self, n: str, id: int, ps: float):
        self.nome = n
        self.idade = id
        self.peso = ps

    def aquecer(self):
        return "Aquecendo..."

    def __str__(self):
        info = f'{self.nome}, {self.idade}, e tem {self.peso} Kg'
        return info

class Corredor(Atleta):
    def correr(self):
        return "correndo..."

class Nadador(Atleta):
    def nadar(self):
        return "nadando..."

class Ciclista(Atleta):
    def pedalar(self):
        return "pedalando..."

class Triatleta(Corredor, Nadador, Ciclista): #HERANÇA MÚLTIPLA
    def realizarMaratona(self):
        info = self.correr()
        info += self.nadar()
        info += self.pedalar()
        return info