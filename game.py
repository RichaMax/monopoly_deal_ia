from player import Player
from cards import Deck
from cards.money import MoneyCard
from cards.property import PropertyCard
from cards.rent import RentCard
from cards.action import DealBreakerCard, DeptCollectionCard, DoubleRentCard, ForcedDealCard, SlyDealCard, \
    RentCard, ItIsMyBirthdayCard, PassGoCard, JustSayNoCard, HouseCard, HotelCard
import json
import numpy as np


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

class Game:
    def __init__(self, players):
        self.players = players
        self.deck = Deck("cards_deck.json")
        self.current_player = 0
        self.game_over = False

    # def next_turn(self):
    #     self.current_player = (self.current_player + 1) % len(self.players)

    # def play(self):
    #     # game loop goes here
    #     while not self.game_over:
    #         player = self.players[self.current_player]
    #         # player's turn goes here
    #         player.draw(self.deck)
    #         # player chooses a card to play
    #         card = choose_card(player)
    #         player.play(card)
    #         self.next_turn()


