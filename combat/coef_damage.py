import random

class CoefDamage:
    @staticmethod
    def check_damage(damage):
        if damage < 0:
            damage = 0
        return damage

    @staticmethod
    def calcul_damage(base_damage):
        return CoefDamage.check_damage(base_damage * random.uniform(0.8, 1.2))

    @staticmethod
    def calculDamage(base_damage):
        return CoefDamage.calcul_damage(base_damage)