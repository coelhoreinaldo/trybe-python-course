class Motorcycle:
    def __init__(self, max_speed: int) -> None:
        self.max_speed = max_speed


class Truck:
    def __init__(self, max_speed: int) -> None:
        self.max_speed = max_speed


def print_max_speed(vehicle: Motorcycle) -> None:
    print(f"Max speed: {vehicle.max_speed} km/h")


print_max_speed(Motorcycle(300))
