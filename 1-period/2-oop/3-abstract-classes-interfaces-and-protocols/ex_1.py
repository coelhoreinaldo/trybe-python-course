import abc


class Person(abc.ABC):
    @abc.abstractmethod
    def print_role(self):
        pass


class Seller(Person):
    def print_role(self):
        print("I am a seller")


class Manager(Person):
    def print_role(self):
        print("I am a manager")
