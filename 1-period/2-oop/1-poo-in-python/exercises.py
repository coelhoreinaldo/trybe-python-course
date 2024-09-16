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
