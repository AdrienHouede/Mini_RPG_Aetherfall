from combat.CoefDamage import CoefDamage
from abc import ABC, abstractmethod

class Personnage(ABC):
    @abstractmethod
    def __init__(self, defense, attack, speed, critical):
        self.hp = 100
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.critical = critical

    def check_damage(self, damage):
        if damage < 0:
            damage = 0
        return damage

    def make_attack(self, target):
        damage = self.attack - target.defense
        damage = CoefDamage.calcul_damage(damage)
        target.hp -= damage
        return damage

    def use_item(self, item):
        attribute = "hp" if item.type == "heal" else item.type
        if hasattr(self, attribute):
            setattr(self, attribute, getattr(self, attribute) + item.value)

    def make_defense(self, value):
        self.defense += value