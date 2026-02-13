class Weapon:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        self.type = "weapon"
        self.attack = 10 * lvl 