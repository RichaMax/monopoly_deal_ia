from .action import ActionCard

rent_value = {"DARK_BLUE": [3, 8],
              "BROWN": [1, 2],
              "LIGHT_GREEN": [1, 2],
              "GREEN": [2, 4, 7],
              "LIGHT_BLUE": [1, 2, 3],
              "ORANGE": [1, 3, 5],
              "PURPLE": [1, 2, 4],
              "RED": [2, 4, 6],
              "YELLOW": [2, 4, 6],
              "BLACK": [1, 2, 3, 4]}


class RentCard(ActionCard):
    def __init__(self, name, value, colors):
        super().__init__(name, value)
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
    def __init__(self, name, value, colors):
        super().__init__(name, value)
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
