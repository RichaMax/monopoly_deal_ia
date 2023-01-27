import json
import numpy as np
from abc import ABC, abstractmethod
from enum import Enum


rent_value = {"DARK_BLUE": [3, 8],
              "BROWN": [1, 2],
              "LIGHT_GREEN": [1, 2],
              "GREEN": [2, 4, 7],
              "LIGHT_BLUE": [1, 2, 3],
              "ORANGE": [1, 3, 5],
              "PURPLE": [1, 2, 4],
              "RED": [2, 4, 6],
              "YELLOW": [2, 4, 6],
              "BLACK": [1, 2, 3, 4]}


class CardType(Enum):
    MONEY = "money"
    PROPERTY = "property"
    ACTION = "action"


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
                    MoneyCard(name=v['attrs']["name"],
                              value=v['attrs']["value"]) for _ in range(v["number_of_cards"])
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
    def __init__(self, card_type, name, value):
        self.card_type = card_type
        self.name = name
        self.value = value

    # @abstractmethod
    # def played(self, active_player, **kwargs):
    #     raise NotImplementedError("played method is not implemented!")

    def __repr__(self):
        return self.name


class MoneyCard(Card):
    def __init__(self, name, value):
        super().__init__(CardType.MONEY, name, value)

    def played(self, active_player):
        active_player.hand.remove(self)
        active_player.money_cards.append(self)
        active_player.money += self.value


class PropertyCard(Card):
    def __init__(self, name, value, color):
        super().__init__(CardType.PROPERTY, name, value)
        self.color = color

    def played(self, active_player):
        active_player.hand.remove(self)
        active_player.properties[self.color].append(self)
        active_player.money += self.value


class JokerPropertyCard(Card):
    def __init__(self, name, value, colors):
        super().__init__(CardType.PROPERTY, name, value)
        self.colors = colors
        self.active_color_pos = None

    def change_color(self, active_player):
        active_player.properties[self.colors[self.active_color_pos]].remove(self)
        self.active_color_pos = 1 - self.active_color_pos
        active_player.properties[self.colors[self.active_color_pos]].append(self)

    # en gros y aura deux action au niveau du joueur pour jouer cette carte, tu la poses c1 ou c2
    def played(self, active_player, chosen_color):
        self.active_color_pos = self.colors.index(chosen_color)
        active_player.hand.remove(self)
        active_player.properties[self.colors[self.active_color_pos]].append(self)
        active_player.money += self.value


class ActionCard(Card):
    def __init__(self, name, value):
        super().__init__(CardType.PROPERTY, name, value)

    def play_as_money(self, active_player):
        active_player.hand.remove(self)
        active_player.money_cards.append(self)
        active_player.money += self.value
#
#     @abstractmethod
#     def specific_action(self, **kwargs):
#         pass
#
#     def played(self, active_player, as_money=False):
#         if as_money:
#             active_player.money += self.value
#             active_player.money_cards.append(self)
#             active_player.hand.remove(self)
#         else:
#             self.specific_action()


class RentCard(ActionCard):
    def __init__(self, name, value, colors):
        super().__init__(name, value)
        self.colors = colors

    def played(self, game, active_player, players_list, chosen_color=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            nb_of_props = len(active_player.properties[chosen_color])
            due_money = rent_value[chosen_color][nb_of_props-1]
            for player in players_list:
                player.pay(active_player, due_money)
            active_player.hand.remove(self)
            game.deck.discard_cards.append(self)


class JokerRentCard(ActionCard):
    def __init__(self, name, value, colors):
        super().__init__(name, value)
        self.colors = colors

    def played(self, game, active_player, targeted_player, chosen_color=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            nb_of_props = len(active_player.properties[chosen_color])
            due_money = rent_value[chosen_color][nb_of_props-1]
            targeted_player.pay(active_player, due_money)
        active_player.hand.remove(self)
        game.deck.discard_cards.append(self)


class DealBreakerCard(ActionCard):
    def __init__(self, name, value, colors):
        super().__init__(name, value)
        self.colors = colors

    def played(self, game, active_player, targeted_player, chosen_color=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            targeted_player.give_group(active_player, chosen_color)
        active_player.hand.remove(self)
        game.deck.discard_cards.append(self)
