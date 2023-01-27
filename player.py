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
            self.money -= 0 # to do
            # player.cash += amount
