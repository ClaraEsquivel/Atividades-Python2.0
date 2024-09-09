import os
os.system("cls||clear")

from enum import Enum

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS ="Recursos humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Sexo(Enum):    
    FEMININO = "Feminino"
    MASCULINO = "Feminino"


class Funcionario:
    def __init__(self, id:int, nome:str, idade:int, salario:float, setor:Setor, sexo:Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return(f"\nId: {self.id}"
               f"\nNome: {self.nome}"
               f"\nIdade: {self.idade}"
               f"\nSalário: {self.salario}"
               f"\nSetor: {self.setor.value}"
               f"\nSexo: {self.sexo.value}"
            )
        
pessoa1 = Funcionario(123, "Paulo", 25, 2500.80, Setor.MARKETING, Sexo.MASCULINO)        
print(pessoa1)

pessoa2 = Funcionario(456, "Maria", 28, 4800.50, Setor.FINANCEIRO, Sexo.FEMININO)
print(pessoa2)



           