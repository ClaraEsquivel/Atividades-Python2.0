from abc import ABC, abstractmethod
import os
os.system("cls||clear")


class Endereco:
    def __init__(self, lagradouro:str, numero:str, complemento:str, cep:str, cidade:str) -> None:
        self.lagradouro = lagradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nLagradouro: {self.lagradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCidade: {self.cidade}"
                 )

# classe abstrata 
class Funcionario(ABC):
    def __init__(self, nome:str, telefone:str, email:str, endereco:Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}" 
            f"\nSalário: {self.salario_final()}"
            f"\n- Endereço - {self.endereco}"
        )

    @abstractmethod
    def salario_final (self) -> float:
        pass
        

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea:str, salario:float, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea
       
    def salario_final(self) -> float: 
        return 3000
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}"
                )
    

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm:str, salario:float, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
        
    def salario_final(self) -> float:
        return 5000

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCRM: {self.crm}"
                )

print("\n= = Dados do Engenheiro = =")
engenheiro1 = Engenheiro("Marcus", "(71)98888-6666", "marcus@gmail.com", "3313", 3000, 
                        Endereco("Liberdade", "564", "Aprt.", "40.028-922", "São Paulo"))
print(engenheiro1)


print("\n = = Dados do Médico = =")
medico1 = Medico("Guilherme", "(71)97777-9999", "guilherme@gmail.com", "A987", 5000, 
                Endereco("Ribeira", "158", "Casa", "40.799-569", "Salvador"))
print(medico1)