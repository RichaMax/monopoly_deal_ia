from .card import Card

class MoneyCard(Card):
    def __init__(self, name, value, card_id):
        super().__init__(name, value, card_id)

    def played(self, active_player):
        active_player.hand.remove(self)
        active_player.money_cards.append(self)
        active_player.money += self.value

class Money1MCard(MoneyCard):
    def __init__(self):
        super().__init__("1M", 1, 1)

class Money2MCard(MoneyCard):
    def __init__(self):
        super().__init__("2M", 2, 2)

class Money3MCard(MoneyCard):
    def __init__(self):
        super().__init__("3M", 3, 3)

class Money4MCard(MoneyCard):
    def __init__(self):
        super().__init__("4M", 4, 4)

class Money5MCard(MoneyCard):
    def __init__(self):
        super().__init__("5M", 5, 5)

class Money10MCard(MoneyCard):
    def __init__(self):
        super().__init__("10M", 10, 6)
