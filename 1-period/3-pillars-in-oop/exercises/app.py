class Vehicle:
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity

    def move(self, distance: int) -> str:
        return (
            f"{self.name} carried {self.capacity} people across {distance} kilometers."
        )


class Car(Vehicle):
    def move(self, distance: int) -> str:
        return super().move(distance)


class Motorcycle(Vehicle):
    def __init__(self, name: str, capacity: int) -> None:
        super().__init__(name, capacity)
        self.capacity = 3

    def move(self, distance: int) -> str:
        return super().move(distance)


car = Car("Car", 5)
print(car.move(100))

motorcycle = Motorcycle("Motorcycle", 2)
print(motorcycle.move(100))
