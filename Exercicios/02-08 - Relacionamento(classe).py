import os
os.system("cls||clear")
    
class Endereco:
    def __init__(self, lagradouro: str, numero: int) -> None:
        self.lagradouro = lagradouro
        self.numero = numero

    #def exibir_endereco(self) -> str:
        # return f"\nLagradouro: {self.lagradouro} \nNúmero: {self.numero}"    

    def __str__(self) -> str:
        return f"\nLagradouro: {self.lagradouro} \nNúmero: {self.numero}"    
        


class Aluno:
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__(self) -> str:
        return f"\nNome: {self.nome} \nIdade: {self.idade} \nEndereço: {self.endereco}"


#endereco1 = Endereco("Rua Pajussara", 970)
#aluno = Aluno("Clara", 21, endereco1)        

aluno1 = Aluno("Clara", 21, Endereco("Rua Pajussara", 970))

print(aluno1)
        