import os
os.system("cls||clear")

class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int, valor: float) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.valor = valor

    def exibir_dados(self) -> str:
        return f"\nTítulo: {self.titulo} \nAutor: {self.autor} \nNúmero de páginas: {self.paginas} \nValor: R${self.valor}"
    
primeiro_livro = Livro("Bruxaria Natural", "Dark Side", 320, 75.00)
segundo_livro = Livro("Todas as suas imperfeições", "Colleen Hoover", 280, 60.00)

print(primeiro_livro.exibir_dados())
print(segundo_livro.exibir_dados())