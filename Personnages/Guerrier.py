from Personnage import Personnages

class Guerrier(Personnages):
    def __init__(self):
        super().__init__(defense=10, attack=1.5, speed=5, critical=0.1)

    def powerfulStrike(self, target):
        damage = self.strength * self.attack * 2 - target.defense
        damage = self.checkDamage(damage)
        target.hp -= damage
        return damage

    def heroicCharge(self, target):
        damage = self.strength * self.attack * 1.5 - target.defense
        damage = self.checkDamage(damage)
        target.hp -= damage
        self.defense += 5
        return damage