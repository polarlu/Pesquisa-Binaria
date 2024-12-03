# Exemplo de um registro de biblioteca com ISBN e nome do livro
class Livro:
    def __init__(self, isbn, nome):
        self.isbn = isbn
        self.nome = nome

    def __repr__(self):
        return f"Livro(ISBN: {self.isbn}, Nome: {self.nome})"

def binary_search_isbn(livros, isbn_target):
    """Realiza uma busca binária em uma lista de livros ordenados por ISBN."""
    left, right = 0, len(livros) - 1

    while left <= right:
        mid = (left + right) // 2
        if livros[mid].isbn == isbn_target:
            return mid  # Retorna o índice do livro encontrado
        elif livros[mid].isbn < isbn_target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Retorna -1 se o livro não for encontrado

# Lista de livros ordenados por ISBN
livros = [
    Livro("0001", "Introdução à Programação"),
    Livro("0002", "Estruturas de Dados"),
    Livro("0003", "Algoritmos e Complexidade"),
    Livro("0004", "Sistemas Operacionais"),
    Livro("0005", "Banco de Dados"),
]

# ISBN a ser procurado
isbn_procurado = "0003"

# Buscando o livro
index = binary_search_isbn(livros, isbn_procurado)
if index != -1:
    livro_encontrado = livros[index]
    print(f"Livro encontrado: {livro_encontrado}")
else:
    print(f"Livro com ISBN {isbn_procurado} não encontrado.")
