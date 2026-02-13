class Weapon():
    def __init__(self, lvl):
        self.equip = False
        self.attack = 10 * lvl

    def equip(self, player):
        if player.inventory is None:
            player.inventory = []
        if not self.equip:
            player.attack += self.attack
            self.equip = True
        return player