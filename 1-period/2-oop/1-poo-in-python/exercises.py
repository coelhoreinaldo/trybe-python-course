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

# Exercício 4
# Escreva uma classe que representa um carro com modelo, ano e velocidade e tem métodos que aceleram e desaceleram sua velocidade, e mostre uma mensagem com o modelo, ano e o valor da aceleração ou desaceleração.


class Car:
    model: str
    year: int
    speed: int

    def __init__(self, model: str, year: int, speed: int) -> None:
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, amount: int = 1):
        self.speed += amount
        print(f"The car {self.model} accelerated {amount} km/h")

    def decelerate(self, amount: int = 1):
        self.speed -= amount
        print(f"The car {self.model} decelerated {amount} km/h")

    def __str__(self) -> str:
        return f"Model: {self.model}, year: {self.year}. Speed: {self.speed}"


car_1 = Car("Fusca", 1970, 0)

car_1.accelerate(4)
car_1.accelerate(4)
car_1.accelerate(4)
car_1.decelerate(2)

print(car_1)
