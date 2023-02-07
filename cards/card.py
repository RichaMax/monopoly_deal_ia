from abc import ABC

class Card(ABC):
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self):
        return self.name