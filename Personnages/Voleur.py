from Personnage import Personnages
import random

class Voleur(Personnages):
    def __init__(self):
        super().__init__(defense=7, attack=1.2, speed=10, critical=0.2)

    def sneakAttack(self, target):
        damage = self.attack - target.defense
        damage = self.checkDamage(damage)
        target.hp -= damage
        return damage

    def perfectDodge(self, value):
        self.speed += value