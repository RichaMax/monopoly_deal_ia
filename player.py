class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.properties = {"DARK_BLUE": [],
                           "BROWN": [],
                           "LIGHT_GREEN": [],
                           "GREEN": [],
                           "LIGHT_BLUE": [],
                           "ORANGE": [],
                           "PURPLE": [],
                           "RED": [],
                           "YELLOW": [],
                           "BLACK": []
                           }
        self.groups = {"DARK_BLUE": {"house": False,
                                     "hotel": False},
                       "BROWN": {"house": False,
                                 "hotel": False},
                       "LIGHT_GREEN": {"house": False,
                                       "hotel": False},
                       "GREEN": {"house": False,
                                 "hotel": False},
                       "LIGHT_BLUE": {"house": False,
                                      "hotel": False},
                       "ORANGE": {"house": False,
                                  "hotel": False},
                       "PURPLE": {"house": False,
                                  "hotel": False},
                       "RED": {"house": False,
                               "hotel": False},
                       "YELLOW": {"house": False,
                                  "hotel": False},
                       "BLACK": {"house": False,
                                 "hotel": False}
                       }
        self.cards_buffer = []
        self.money = 0
        self.money_cards = []

    def draw(self, deck, nb_cards):
        for _ in range(nb_cards):
            card = deck.draw()
            self.hand.append(card)

    def play(self, card):
        self.hand.remove(card)
        card.played()

    def pay(self, player, amount):
        if self.money > 0:
            self.money -= 0  # to do
            # player.cash += amount
