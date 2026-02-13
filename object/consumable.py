class Consumable:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        self.type = "heal"
        self.value = 10 * lvl
