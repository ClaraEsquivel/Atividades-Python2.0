from abc import ABC, abstractmethod

import os
os.system("cls||clear")

class ValorNegativoError(Exception):
    pass

class Endereco:
    def __init__(self, lagradouro:str, numero:str, cidade:str) -> None:
        self.lagradouro = lagradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return(
            f"\nLagradouro: {self.lagradouro}"
            f"\nNúmero: {self.numero}"
            f"\nCidade: {self.cidade}"
                )
    
class Funcionario(ABC):
    def __init__(self, nome:str, email:str, endereco:Endereco) -> None:
        self.nome = nome
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return(
            f"\nNome: {self.nome}"
            f"\nEmail: {self.email}"
            f"\n= Endereço = {self.endereco}"
                )    
    
    @abstractmethod
    def salario_final (self) -> float:
        pass


    def salario (self,valor):
        try:
            self.__verificar_salario(valor)
        except ValorNegativoError as error:
            return f"Erro: {error}"    
        
    def __verificar_salario(self,valor):
        if valor < 0:
            raise ValorNegativoError("Não é possível inserir um salário")
