from .card import Card

group_sizes = {"DARK_BLUE": 2,
               "BROWN": 2,
               "LIGHT_GREEN": 2,
               "GREEN": 4,
               "LIGHT_BLUE": 2,
               "ORANGE": 2,
               "PURPLE": 2,
               "RED": 3,
               "YELLOW": 3,
               "BLACK": 2
               }


class IllegalMove(Exception):
    pass


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

    def played(self, active_player, targeted_player, chosen_color=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            active_player.cards_buffer.extend(targeted_player.properties[chosen_color])
            targeted_player.properties[chosen_color] = []


class DeptCollectionCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, active_player, targeted_player, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            targeted_player.pay(active_player, 5)


class DoubleRentCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, active_player, rent_card=None, players_list=None, chosen_color=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            rent_card.played(active_player, players_list, chosen_color, double=True)


class ForcedDealCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, active_player, targeted_player=None, ap_color_a_card=None, tp_color_a_card=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            targeted_player.properties[tp_color_a_card[0]].remove(tp_color_a_card[1])
            active_player.cards_buffer.append(tp_color_a_card[1])

            active_player.properties[ap_color_a_card[0]].remove(ap_color_a_card[1])
            targeted_player.properties[ap_color_a_card[0]].append(ap_color_a_card[1])


class SlyDealCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, active_player, targeted_player, tp_color_a_card, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            targeted_player.properties[tp_color_a_card[0]].remove(tp_color_a_card[1])
            active_player.cards_buffer.append(tp_color_a_card[1])


class HouseCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, active_player, chosen_color=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            if len(active_player.properties[chosen_color]) == group_sizes[chosen_color]:
                if not active_player.groups[chosen_color]["house"]:
                    active_player.groups[chosen_color]["house"] = True
                else:
                    raise IllegalMove(f"{active_player.name} - {chosen_color} - All ready have house")
            else:
                raise IllegalMove(f"{active_player.name} - {chosen_color} - Not a full group: "
                                  f"{len(active_player.properties[chosen_color])} vs {group_sizes[chosen_color]}")


class HotelCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, active_player, chosen_color=None, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            active_player.groups[chosen_color]["hotel"] = True
            if not active_player.groups[chosen_color]["house"]:
                raise IllegalMove(f"{active_player.name} - {chosen_color} - Do not have a house")
            else:
                active_player.groups[chosen_color]["hotel"] = True


class ItIsMyBirthdayCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, active_player, players_list, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            for player in players_list:
                player.pay(active_player, 2)


class JustSayNoCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, active_player, as_money=False):
        if as_money:
            self.play_as_money(active_player)


class PassGoCard(ActionCard):
    def __init__(self, name, value):
        super().__init__(name, value)

    def played(self, active_player, deck, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            active_player.draw(deck, 2)
