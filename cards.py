from abc import ABC, abstractmethod


class Card(ABC):
    """
    to write
    """
    def __init__(self, card_type, name, value):
        self.card_type = card_type
        self.name = name
        self.value = value

    @abstractmethod
    def play(self, **kwargs):
        raise NotImplementedError("Play method is not implemented!")

    def __repr__(self):
        return self.name


class MoneyCard(Card):
    def __init__(self, name, value):
        super().__init__("money", name, value)

    def play(self, player_obj):
        player_obj.money += self.value
        player_obj.money_card.append(self)


class ProprietyCard(Card):
    def __init__(self, name, value, color, multi=False, joker=False):
        super().__init__("property", name, value)
        self.color = color
        self.is_multi = multi
        self.is_joker = joker


class ActionCard(Card):
    def __init__(self, name, value, action):
        super().__init__("action", name, value)
        self.action = action


class RentCard(ActionCard):
    def __init__(self, name, value, colors, action):
        super().__init__(name, value, action)
        self.card_type = "rent"
        self.colors = colors
