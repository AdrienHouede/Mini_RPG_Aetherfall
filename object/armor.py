class Armor:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        self.type = "armor"
        self.defense = 10 * lvl
