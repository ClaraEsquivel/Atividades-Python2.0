import os

os.system("cls||clear") # Limpar o terminal.

class Aluno:
   # uma função dentro de uma classe não é uma função e sim um metodo.
   # Construtor.
    def __init__(self, nome: str, idade: int) -> None:
        # Atributos.
        self.nome = nome
        self.idade = idade

    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}"
        
# Instanciar classe.
aluno = Aluno("Clara", 21)

# print(f"Nome: {aluno.nome}")
# print(f"Idade: {aluno.idade}")

print(aluno.exibir_dados())