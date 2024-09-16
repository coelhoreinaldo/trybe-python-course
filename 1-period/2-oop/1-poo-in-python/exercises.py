# Exercício 1
# Escreva uma função que recebe uma lista de inteiros e retorna a soma desses valores.


def sum_integers(integers: list[int]) -> int:
    return sum(integers)


sum_integers([1, 2, 3, 4, 5])

# Exercício 2
# Escreva uma função que recebe uma lista de strings e um caractere e retorna uma lista com as strings que começam com o caractere fornecido.


def find_str(strings: list[str], char: str) -> list[str]:
    return [s for s in strings if char in s]


animals = ["cachorro", "gato", "elefante", "girafa"]
char = "g"

find_str(animals, char)

# Exercício 3
# Escreva uma classe que representa um livro com título, autor e número de páginas e altere o método __str__ para uma string que descreve o livro.


class Book:
    title: str
    author: str
    pages: int

    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return (
            f"Title: {self.title}, author: {self.author}. Number of pages: {self.pages}"
        )


book = Book("title", "author", 60)

print(book)
