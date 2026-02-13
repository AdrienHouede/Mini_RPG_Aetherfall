import random

class CoefDamage:
    def check_damage(damage):
        if damage < 0:
            damage = 0
        return damage

    def calcul_damage(self, base_damage):
        return self.check_damage(base_damage * random.uniform(0.8, 1.2))