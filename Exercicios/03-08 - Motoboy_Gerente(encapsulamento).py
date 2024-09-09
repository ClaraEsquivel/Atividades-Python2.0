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
    def __init__(self, nome:str, email:str, salario:float, endereco:Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    def __str__(self) -> str:
        return(
            f"\nNome: {self.nome}"
            f"\nEmail: {self.email}"
            f"\nSálario: {self.salario}"
            f"\n= Endereço = {self.endereco}"
                )    
    
    @abstractmethod
    def salario_final (self) -> float:
        pass

    def salario_final(self,valor):
        try:
            self.__verificar_salario(valor)
        except ValorNegativoError as error:
            return f"Erro: {error}"   

        return self.salario
        
    def __verificar_salario(self,valor):
        if valor < 0:
            raise ValorNegativoError("Não é possível inserir um salário negativo")



class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, cnh:str, salario:float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh
        

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCNH: {self.cnh}"
                )
        

class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario:float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)
       


motoboy1 = Motoboy("João", "joao@gmail.com", "A", 2000, Endereco("Castelo Branco", "123", "Salvador"))
print(motoboy1)
# print("= Salário =")
print(motoboy1.salario_final(2000))

gerente1 = Gerente("Pedro", "pedro@gmail.com", 5000, Endereco("Liberdade", "115", "São Paulo"))
print(gerente1)
# print("= Salário =")
print(gerente1.salario_final(-5000))