from abc import ABC


class Card(ABC):
    def __init__(self, name: str, value: int, card_id: int):
        self.name = name
        self.value = value
        self.card_id = card_id

    def __repr__(self):
        return self.name