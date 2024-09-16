def add_two_numbers(num1: int, num2: int) -> int:
    return num1 + num2


class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height


class Database:
    pass


database_1 = Database()
database_2 = Database()


class Car:
    def __init__(self, brand: str, model: str, year: int, color: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def identify(self):
        print(
            f"Meu carro é um {self.model}, da {self.brand}. Ele é do ano {self.year} e tem a cor {self.color}"
        )


car_1 = Car("Chevrolet", "Onix", 2020, "Preto")
car_1.identify()
