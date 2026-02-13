from personnages.personnage import Personnage
import random

class Voleur(Personnage):
    def __init__(self):
        super().__init__(defense=7, attack=1.2, speed=10, critical=0.2)

    def sneak_attack(self, target):
        damage = self.attack - target.defense
        damage = self.check_damage(damage)
        target.hp -= damage
        return damage

    def perfect_dodge(self, value):
        self.speed += value