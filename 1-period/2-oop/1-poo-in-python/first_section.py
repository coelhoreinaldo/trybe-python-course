from typing import Optional, Union


def add_two_numbers(num1: int, num2: int) -> int:
    return num1 + num2


class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height


"""
>>> Database(
...     dialect = "",
...     user = "",
...     host = "",
...     password = "",
...     database = "",
... )
Traceback (most recent call last):
...
ValueError: invalid default `port` for unrecognized `dialect`

>>> print(Database(
...     dialect = "postgres",
...     user = "tryber",
...     host = "trybe",
...     password = "i_love_python",
...     database = "computer_science",
... ).connection_url)
postgres://tryber:i_love_python@trybe:5432/computer_science
"""


class Database:
    def __init__(
        self,
        dialect: str,
        user: str,
        host: str,
        password: str,
        database: str,
        port: Optional[Union[str, int]],
    ) -> None:
        self.connection_url = f"{dialect}://{user}:{password}@{host}:{port}/{database}"


database_1 = Database(
    dialect="dialect",
    user="user",
    host="host",
    password="password",
    database="database",
    port=5432,
)
print(database_1.connection_url)


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
