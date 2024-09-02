from abc import ABC, abstractmethod
import os

os.system("cls||clear")

class Funcionario(ABC): 
    # construtor
    def __init__(self, nome:str, idade:int, salario:float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod #classe abstrata
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.2 #Acréscimo de 20%
        salario_final = self.salario * BONIFICACAO
        return salario_final


class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh:str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        BONIFICACAO = 1.1 #Acréscimo de 20%
        salario_final = self.salario * BONIFICACAO
        return salario_final



#Instanciando
gerente1 = Gerente("Gabriel", 30, 3000.0) 
print("\nGerente")
print(f"Nome: {gerente1.nome}")
print(f"Salário final: {gerente1.calcular_salario()}")

motoboy1 = Motoboy("Miguel", 30, 1000.0, "A") 
print("\nMotoboy")
print(f"Nome: {motoboy1.nome}")
print(f"CNH: {motoboy1.cnh}")
print(f"Salário final: {motoboy1.calcular_salario()}")



    