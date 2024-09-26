from abc import ABC, abstractmethod


class Customer:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone


class Address:
    def __init__(self, street: str, number: int, city: str, state: str):
        self.street = street
        self.number = number
        self.city = city
        self.state = state


class Deliverable(ABC):
    @abstractmethod
    def delivery(self, customer: Customer, address: Address) -> None:
        pass


class Mail(Deliverable):
    def delivery(self, customer: Customer, address: Address):
        print(
            f"Mail delivered to {customer.name} at {address.street}, {address.number} - {address.city}/{address.state}"
        )


class ShippingCompany(Deliverable):
    def delivery(self, customer: Customer, address: Address):
        print(
            f"Package delivered to {customer.name} at {address.street}, {address.number} - {address.city}/{address.state}"
        )


def main():
    mail = Mail()
    shipping_company = ShippingCompany()

    customer = Customer("Rafa", "999999999")
    address = Address("Rua A", 100, "São Paulo", "SP")

    mail.delivery(customer, address)
    shipping_company.delivery(customer, address)


if __name__ == "__main__":
    main()
