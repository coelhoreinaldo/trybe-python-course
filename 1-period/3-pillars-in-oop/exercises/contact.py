class Contact:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email


class ContactList:
    contacts: list[Contact]
    favorites: list[Contact]

    def __init__(self) -> None:
        self.contacts = []
        self.favorites = []

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def remove_contact(self, name: str) -> Contact:
        for index, contact in enumerate(self.contacts):
            if contact.name == name:
                return self.contacts.pop(index)
        raise LookupError(f"Contact {name} not found")

    def add_to_favorites(self, name: str) -> None:
        for index, contact in enumerate(self.contacts):
            if contact.name == name:
                self.favorites.append(self.contacts.pop(index))
                return
        raise LookupError(f"Contact {name} not found")

    def remove_from_favorites(self, name: str) -> None:
        for index, contact in enumerate(self.favorites):
            if contact.name == name:
                self.contacts.append(self.favorites.pop(index))
                return
        raise LookupError(f"Contact {name} not found")
