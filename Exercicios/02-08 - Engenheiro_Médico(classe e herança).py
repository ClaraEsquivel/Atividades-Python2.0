from abc import ABC, abstractmethod
import os
os.system("cls||clear")

class Endereco:
    def __init__(self, lagradouro:str, numero:str, complemento:str, cep:str, cidade:str) -> None:
        self.lagradouro - lagradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return f"\nLagradouro: {self.lagradouro} \nNúmero: {self.numero}"  
    
class Funcionario(ABC)    :
    def __init__(self, nome:str, telefone:str, email:str, endereco:Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod #classe abstrata
    def calcular_salario(self) -> float:
        pass
        
        