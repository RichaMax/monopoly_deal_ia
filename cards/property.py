from .card import Card


class PropertyCard(Card):
    def __init__(self, name, value, card_id, color):
        super().__init__(name, value, card_id)
        self.color = color

    def played(self, active_player):
        active_player.properties[self.color].append(self)
        active_player.money += self.value


class JokerPropertyCard(Card):
    def __init__(self, name, value, card_id, colors):
        super().__init__(name, value, card_id)
        self.colors = colors
        self.active_color_pos = None

    def change_color(self, active_player):
        active_player.properties[self.colors[self.active_color_pos]].remove(
            self)
        self.active_color_pos = 1 - self.active_color_pos
        active_player.properties[self.colors[self.active_color_pos]].append(
            self)

    # en gros y aura deux action au niveau du joueur pour jouer cette carte, tu la poses c1 ou c2
    def played(self, active_player, chosen_color):
        self.active_color_pos = self.colors.index(chosen_color)
        active_player.properties[self.colors[self.active_color_pos]].append(
            self)
        active_player.money += self.value


class PropertyDarkBlueCard(PropertyCard):
    def __init__(self):
        super().__init__("Dark Blue", 4, 7, ["DARK_BLUE"])


class PropertyBrownCard(PropertyCard):
    def __init__(self):
        super().__init__("Brown", 1, 8, ["BROWN"])


class PropertyLightGreenCard(PropertyCard):
    def __init__(self):
        super().__init__("Light Green", 2, 9, ["LIGHT_GREEN"])


class PropertyGreenCard(PropertyCard):
    def __init__(self):
        super().__init__("Green", 4, 10, ["GREEN"])


class PropertyLightBlueCard(PropertyCard):
    def __init__(self):
        super().__init__("Light Blue", 2, 11, ["LIGHT_BLUE"])


class PropertyOrangeCard(PropertyCard):
    def __init__(self):
        super().__init__("Orange", 2, 12, ["ORANGE"])


class PropertyPurpleCard(PropertyCard):
    def __init__(self):
        super().__init__("Purple", 2, 13, ["PURPLE"])


class PropertyRedCard(PropertyCard):
    def __init__(self):
        super().__init__("Red", 3, 14, ["RED"])


class PropertyYellowCard(PropertyCard):
    def __init__(self):
        super().__init__("Yellow", 3, 15, ["YELLOW"])


class PropertyBlackCard(PropertyCard):
    def __init__(self):
        super().__init__("Black", 2, 16, ["BLACK"])


class JokerPropertyDarkBlueGreenCard(JokerPropertyCard):
    def __init__(self):
        super().__init__("Dark Blue/Green", 4, 17, ["DARK_BLUE", "GREEN"])


class JokerPropertyBrownLightBlueCard(JokerPropertyCard):
    def __init__(self):
        super().__init__("Brown/Light Blue", 1, 18, ["BROWN", "LIGHT_BLUE"])


class JokerPropertyPurpleOrangeCard(JokerPropertyCard):
    def __init__(self):
        super().__init__("Purple/Orange", 2, 19, ["PURPLE", "ORANGE"])


class JokerPropertyRedYellowCard(JokerPropertyCard):
    def __init__(self):
        super().__init__("Red/Yellow", 3, 20, ["RED", "YELLOW"])


class JokerPropertyBlackLightGreenCard(JokerPropertyCard):
    def __init__(self):
        super().__init__("Black/Light Green", 2, 21, ["BLACK", "LIGHT_GREEN"])


class JokerPropertyBlackLightBlueCard(JokerPropertyCard):
    def __init__(self):
        super().__init__("Black/Light Blue", 4, 22, ["BLACK", "LIGHT_BLUE"])


class JokerPropertyGreenBlackCard(JokerPropertyCard):
    def __init__(self):
        super().__init__("Green/Black", 4, 23, ["GREEN", "BLACK"])


class JokerPropertyAllColors(JokerPropertyCard):
    def __init__(self):
        super().__init__("All", 0, 24, ["DARK_BLUE", "BROWN", "LIGHT_GREEN",
                                        "GREEN", "LIGHT_BLUE", "ORANGE", "PURPLE", "RED", "YELLOW", "BLACK"])
