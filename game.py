from .utils import groups_size
from .player import Player


class MonopolyDeal:
    def __init__(self, players_list, deck):
        self.players = players_list
        self.current_player = None
        self.states_space = None  # je sais pas encore, je pense une space matrix
        self.action_space = None # je sais pas encore
        self.deck = deck

    def reset(self):
        pass

    def is_winner(self, player):
        nb_of_groups = 0
        for color, size in groups_size.items():
            if len(player.properties[color]) != size:
               nb_of_groups += 1
        return nb_of_groups >= 3

    def step(self, action):
        # TODO: all
        return
