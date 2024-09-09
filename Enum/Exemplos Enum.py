from enum import Enum

import os
os.system("cls||clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa:
    def __init__(self, nome:str, idade:int, sexo:Sexo ) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


    def __str__(self) -> str:
        return (f"\n Nome: {self.nome}"
                f"\n Idade: {self.idade}"
                f"\n Sexo: {self.sexo.value}"
                #value = valor que demos a variável
                )
    
# Instanciando classe Pessoa
pessoa1 = Pessoa("Clara", 21, Sexo.FEMININO)
print(pessoa1)

pessoa2 = Pessoa("Miguel", 18, Sexo.MASCULINO)
print(pessoa2)
