import gym
from gym import spaces
import random

from .utils import groups_size
from .player import Player


class MonopolyDeal(gym.Env):
    def __init__(self, players_list, deck):
        self.players = random.huffle(players_list)
        self.current_player = self.players[0]
        self.deck = deck
        # TODO: evalute the best trade off between full information and partial information
        # draw, play money, play property, play action, end turn
        self.action_space = spaces.Discrete(5)

        self.observation_space = spaces.Dict({
            "deck": spaces.Discrete(len(self.deck.cards)), # cards left in deck
            "hand": spaces.MultiDiscrete([6, 5, 3, 3, 2, 1, # money cards
                                          2, 2, 2, 3, 3, 3, 3, 3, 3, 4, # property cards
                                          1, 1, 2, 2, 1, 1, 1, 2, # property joker cards
                                          2, 2, 2, 2, 2, 3, # rent cards
                                          2, 3, 2, 3, 3, 3, 10, 3, 3, 2 # action cards
                                          ]),
            "money": spaces.Tuple(spaces.Discrete(len(self.deck.cards)),
                                 (spaces.MultiDiscrete([6, 5, 3, 3, 2, 1]))),
            "property_sets": spaces.MultiBinary(len(self.property_sets))
        })

    def next_player(self):
        self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]
    
    #TODO: refactor this
    def _get_observation(self):
        hand = [c.card_id for c in self.current_player.hand]
        property_sets = []
        # for color, cards in self.property_sets.items():
        #     property_sets.append(int(self.current_player in cards))
        return {
            "deck": len(self.deck.cards),
            "hand": [hand.count(i+1) for i in range(41)],
            "property_sets": property_sets
        }
    
    def reset(self):
        pass

    def _check_for_win(self):
        nb_of_groups = 0
        for color, size in groups_size.items():
            if len(self.current_player.properties[color]) != size:
               nb_of_groups += 1
        return nb_of_groups >= 3

    # RAW chatgpt step => to modify & improve
    def step(self, action):
        player = self.players[self.current_player]
        reward = 0
        done = False
        info = {}
        
        if action == 0: # draw card
            player.draw(self.deck, 2)
            reward = 1
        elif action == 1: # play property
            card = choose_property_card(player)
            player.play(card)
            self.property_sets[card.color].add(player)
            if self._check_for_win():
                reward = 100
                done = True
            else:
                reward = 10
        elif action == 2: # play action
            card = choose_action_card(player)
            player.play(card)
            if self._check_for_win():
                reward = 100
                done = True
            else:
                reward = 5
        elif action == 3: # end turn
            self.current_player = (self.current_player + 1) % len(self.players)
            reward = 0
        
        observation = self._get_observation()
        return observation, reward, done, info
