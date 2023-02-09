from player import Player
from cards.money import Money1MCard, Money2MCard, Money3MCard, Money4MCard, Money5MCard, Money10MCard
from cards.property import PropertyBlackCard, PropertyBrownCard, PropertyDarkBlueCard, PropertyGreenCard, \
    PropertyLightBlueCard, PropertyLightGreenCard, PropertyOrangeCard, PropertyPurpleCard, PropertyRedCard, \
    PropertyYellowCard, JokerPropertyBlackLightGreenCard, JokerPropertyBrownLightBlueCard, JokerPropertyDarkBlueGreenCard, \
    JokerPropertyPurpleOrangeCard, JokerPropertyRedYellowCard, JokerPropertyAllColors, JokerPropertyBlackLightBlueCard, \
    JokerPropertyGreenBlackCard
from cards.rent import RentDarkBlueGreenCard, RentBlackLightGreenCard, RentBrownLightBlueCard, RentPurpleOrangeCard, \
    RentRedYellowCard, JokerRentAllColors
from cards.action import DealBreakerCard, DeptCollectionCard, DoubleRentCard, ForcedDealCard, SlyDealCard, \
    ItIsMyBirthdayCard, PassGoCard, JustSayNoCard, HouseCard, HotelCard
import json
import numpy as np


class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        self.shuffle()
        self.discard_cards = []

    def shuffle(self):
        np.random.shuffle(self.cards)

    def generate_deck(self):
        return [Money1MCard() for _ in range(6)] + [Money2MCard() for _ in range(5)] + \
               [Money3MCard() for _ in range(3)] + [Money4MCard() for _ in range(3)] + \
               [Money5MCard() for _ in range(2)] + [Money10MCard() for _ in range(1)] + \
               [PropertyBlackCard() for _ in range(4)] + [PropertyBrownCard() for _ in range(2)] + \
               [PropertyDarkBlueCard() for _ in range(2)] + [PropertyGreenCard() for _ in range(3)] + \
               [PropertyLightBlueCard() for _ in range(3)] + [PropertyLightGreenCard() for _ in range(2)] + \
               [PropertyOrangeCard() for _ in range(3)] + [PropertyPurpleCard() for _ in range(3)] + \
               [PropertyRedCard() for _ in range(3)] + [PropertyYellowCard() for _ in range(3)] + \
               [JokerPropertyBlackLightGreenCard() for _ in range(1)] + \
               [JokerPropertyBrownLightBlueCard() for _ in range(1)] + \
               [JokerPropertyDarkBlueGreenCard() for _ in range(1)] + \
               [JokerPropertyPurpleOrangeCard() for _ in range(2)] + \
               [JokerPropertyRedYellowCard() for _ in range(2)] + \
               [JokerPropertyAllColors() for _ in range(2)] + \
               [JokerPropertyBlackLightBlueCard() for _ in range(1)] + \
               [JokerPropertyGreenBlackCard() for _ in range(1)] + \
               [RentDarkBlueGreenCard() for _ in range(2)] + [RentBlackLightGreenCard() for _ in range(2)] + \
               [RentBrownLightBlueCard() for _ in range(2)] + [RentPurpleOrangeCard() for _ in range(2)] + \
               [RentRedYellowCard() for _ in range(2)] + [JokerRentAllColors() for _ in range(3)] + \
               [DealBreakerCard('Deal Breaker', 5) for _ in range(2)] + \
               [DeptCollectionCard('Dept Collection', 3) for _ in range(3)] + \
               [DoubleRentCard('Double Rent', 1) for _ in range(2)] + \
               [ForcedDealCard('Forced Deal', 3) for _ in range(3)] + \
               [SlyDealCard("Sly Deal", 3) for _ in range(3)] + \
               [ItIsMyBirthdayCard("Birthday", 2) for _ in range(3)] + [PassGoCard("Pass Go", 1) for _ in range(10)] + \
               [JustSayNoCard("No", 4) for _ in range(3)] + \
               [HouseCard("House", 3) for _ in range(3)] + [HotelCard("Hotel", 4) for _ in range(3)]

    def draw(self):
        return self.cards.pop()


class Game:
    def __init__(self, players_list):
        self.players = players_list
        self.deck = Deck("cards_deck.json")
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


