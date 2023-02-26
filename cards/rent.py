from .action import ActionCard
from ..utils import rent_value


class RentCard(ActionCard):
    def __init__(self, name, value, card_id, colors):
        super().__init__(name, value, card_id)
        self.colors = colors

    def played(self, active_player, players_list=None, chosen_color=None, double=False, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            nb_of_props = len(active_player.properties[chosen_color])
            due_money = rent_value[chosen_color][nb_of_props - 1]
            if double:
                due_money *= 2
            for player in players_list:
                player.pay(active_player, due_money)


class JokerRentCard(ActionCard):
    def __init__(self, name, value, card_id, colors):
        super().__init__(name, value, card_id)
        self.colors = colors

    def played(self, active_player, targeted_player=None, chosen_color=None, double=False, as_money=False):
        if as_money:
            self.play_as_money(active_player)
        else:
            nb_of_props = len(active_player.properties[chosen_color])
            due_money = rent_value[chosen_color][nb_of_props - 1]
            if double:
                due_money *= 2
            targeted_player.pay(active_player, due_money)


class RentDarkBlueGreenCard(RentCard):
    def __init__(self):
        super().__init__("Rent Dark Blue - Green", 1, 25, ["DARK_BLUE", "GREEN"])

class RentBrownLightBlueCard(RentCard):
    def __init__(self):
        super().__init__("Rent Brown - Light Blue", 1, 26, ["BROWN", "LIGHT_BLUE"])

class RentPurpleOrangeCard(RentCard):
    def __init__(self):
        super().__init__("Rent Purple - Orange", 1, 27, ["PURPLE", "ORANGE"])

class RentRedYellowCard(RentCard):
    def __init__(self):
        super().__init__("Rent Red - Yellow", 1, 28, ["RED", "YELLOW"])

class RentBlackLightGreenCard(RentCard):
    def __init__(self):
        super().__init__("Rent Black - Light Green", 1, 29, ["BLACK", "LIGHT_GREEN"])

class JokerRentAllColors(JokerRentCard):
    def __init__(self):
        super().__init__("Joker Rent All", 3, 30, ["DARK_BLUE", "BROWN", "LIGHT_GREEN", "GREEN", "LIGHT_BLUE", "ORANGE", "PURPLE", "RED", "YELLOW", "BLACK"])
