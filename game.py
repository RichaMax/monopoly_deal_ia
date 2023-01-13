from player import Player
from yaml.loader import SafeLoader
from cards import Deck


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


