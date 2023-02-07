from .card import Card

class ActionCard(Card):
    def __init__(self, name, value):
        super().__init__(name, value)

    def play_as_money(self, active_player):
        active_player.hand.remove(self)
        active_player.money_cards.append(self)
        active_player.money += self.value


class DealBreakerCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, game, active_player, targeted_player, chosen_color=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            targeted_player.give_group(active_player, chosen_color)
        active_player.hand.remove(self)
        game.deck.discard_cards.append(self)


class DeptCollectionCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, game, active_player, targeted_player, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            targeted_player.pay(active_player, 5)
        active_player.hand.remove(self)
        game.deck.discard_cards.append(self)


class DoubleRentCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, game, active_player, rent_card=None, players_list=None, chosen_color=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            rent_card.played(active_player, players_list, chosen_color, double=True)
        active_player.hand.remove(self)
        game.deck.discard_cards.append(self)


class ForcedDealCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, game, active_player, targeted_player=None, ap_color_a_card=None, tp_color_a_card=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            targeted_player.properties[tp_color_a_card[0]].remove(tp_color_a_card[1])
            active_player.properties[tp_color_a_card[0]].append(tp_color_a_card[1])

            active_player.properties[ap_color_a_card[0]].remove(ap_color_a_card[1])
            targeted_player.properties[ap_color_a_card[0]].append(ap_color_a_card[1])

        active_player.hand.remove(self)
        game.deck.discard_cards.append(self)