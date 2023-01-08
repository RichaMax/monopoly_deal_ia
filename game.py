import random
from player import Player
import yaml
from yaml.loader import SafeLoader


class Game:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.current_player = 0

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def play(self):
        # game loop goes here
        while not game_over:
            player = self.players[self.current_player]
            # player's turn goes here
            player.draw(self.deck)
            # player chooses a card to play
            card = choose_card(player)
            player.play(card)
            self.next_turn()


class Deck:
    def __init__(self):
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)