from Personnage import Personnages

class Mage(Personnages):
    def __init__(self):
        super().__init__(defense=5, attack=2, speed=7, critical=0.05)

    def fireball(self, target):
        damage = self.strength * self.attack * 1.5 - target.defense
        damage = self.checkDamage(damage)
        target.hp -= damage
        return damage

    def arcaneShield(self, value):
        self.defense += value