import json
import random
from abc import ABC, abstractmethod


class Deck:
    def __init__(self):
        self.cards = []
        self.discard_carss = []
        self.shuffle()

    def shuffle(self):
        self.cards = random.shuffle(self.cards)

    def generate_deck(self, path_to_deck):
        with open(path_to_deck, 'rb') as f:
            cards_dict = json.load(f)
        for k, v in cards_dict.items():
            pass
        print(cards_dict)

    def draw(self):
        return self.cards.pop()


class Card(ABC):
    """
    to write
    """
    def __init__(self, card_type, name, value):
        self.card_type = card_type
        self.name = name
        self.value = value

    @abstractmethod
    def played(self, **kwargs):
        raise NotImplementedError("Play method is not implemented!")

    def __repr__(self):
        return self.name


class MoneyCard(Card):
    def __init__(self, name, value):
        super().__init__("money", name, value)

    def played(self, player_obj):
        player_obj.money += self.value
        player_obj.money_cards.append(self)


class ProprietyCard(Card):
    def __init__(self, name, value, color, rent_values, multi=False):
        super().__init__("property", name, value)
        self.color = color
        self.is_multi = multi
        self.rent_values = rent_values


class ActionCard(Card):
    def __init__(self, name, value, action):
        super().__init__("action", name, value)
        self.action = action
    
    def played(self, player_obj, as_money=False):
        if as_money:
            player_obj.money += self.value
            player_obj.money_cards.append(self)
        else:
            pass


class RentCard(ActionCard):
    def __init__(self, name, value, colors, action, rent_values):
        super().__init__(name, value, action)
        self.card_type = "rent"
        self.colors = colors


    def played(self, player_obj, as_money=False):
        if as_money:
            player_obj.money += self.value
            player_obj.money_cards.append(self)
        else:
            pass