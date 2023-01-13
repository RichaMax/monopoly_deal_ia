import json
import numpy as np
from abc import ABC, abstractmethod


class Deck:
    def __init__(self, path_to_deck):
        self.cards = self.generate_deck(path_to_deck)
        self.shuffle()
        self.discard_cards = []

    def shuffle(self):
        np.random.shuffle(self.cards)

    def generate_deck(self, path_to_deck):
        deck = []
        with open(path_to_deck, 'rb') as f:
            cards_dict = json.load(f)
        for k, v in cards_dict.items():
            if "money" in k:
                deck += [
                    MoneyCard(name=v['attrs']["name"], value=v['attrs']["value"]) for _ in range(v["number_of_cards"])
                ]
            elif k.startswith("rent"):
                deck += [
                    RentCard(name=v['attrs']["name"],
                             value=v['attrs']["value"],
                             colors=v['attrs']["colors"],
                             action=v['attrs']["action"]) for _ in range(v["number_of_cards"])
                ]
            elif k.startswith("property"):
                deck += [
                    PropertyCard(name=v['attrs']["name"],
                                 value=v['attrs']["value"],
                                 color=v['attrs']["color"],
                                 rent_values=v['attrs']["rent_values"],
                                 multi=v['attrs']["multi"]) for _ in range(v["number_of_cards"])
                ]
            else:
                deck += [
                    ActionCard(name=v['attrs']["name"],
                               value=v['attrs']["value"],
                               action=v['attrs']["action"]) for _ in range(v["number_of_cards"])
                ]
        return deck

    def draw(self):
        return self.cards.pop()

# 
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
        raise NotImplementedError("played method is not implemented!")

    def __repr__(self):
        return self.name


class MoneyCard(Card):
    def __init__(self, name, value):
        super().__init__("money", name, value)

    def played(self, player_obj):
        player_obj.money += self.value
        player_obj.money_cards.append(self)

#faire un dic pour dagager les valeurs du rent des cartes
class PropertyCard(Card):
    def __init__(self, name, value, color, rent_values, multi=False):
        super().__init__("property", name, value)
        self.color = color
        self.is_multi = multi
        self.rent_values = rent_values

    def played(self, player_obj):
        pass

# faire une class par action card
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
    def __init__(self, name, value, colors, action):
        super().__init__(name, value, action)
        self.card_type = "rent"
        self.colors = colors

    def played(self, player_obj, as_money=False, target=None):
        if as_money:
            player_obj.money += self.value
            player_obj.money_cards.append(self)
        else:
            pass
