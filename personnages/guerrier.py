from personnages.personnage import Personnage

class Guerrier(Personnage):
    def __init__(self):
        super().__init__(defense=10, attack=1.5, speed=5, critical=0.1)

    def powerful_strike(self, target):
        damage = self.attack * 2 - target.defense
        damage = self.check_damage(damage)
        target.hp -= damage
        return damage

    def heroic_charge(self, target):
        damage = self.attack * 1.5 - target.defense
        damage = self.check_damage(damage)
        target.hp -= damage
        self.defense += 5
        return damage