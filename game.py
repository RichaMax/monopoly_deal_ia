from player import Player


class MonopolyDeal:
    def __init__(self, players_list):
        self.players = players_list
        self.current_player = None
        self.observation_space = None # je sais pas encore
        self.action_space = None # je sais pas encore
        self.game_status = None # je sais pas encore, je pense une space matrix

    def reset(self):
        

    def start(self):
        self.turn = 1

    def next_turn(self):
        self.turn += 1
        self.current_player = self.players[self.turn % len(self.players)]

    def have_winner(self):
        for player in self.players:
            if player.

    def step(self, action):
        self.current_player.take_turn()
        # TODO: all
        return 