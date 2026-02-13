import random

class CoefDamage:
    def checkDamage(damage):
        if damage < 0:
            damage = 0
        return damage

    def calculDamage(self, baseDamage):
        return self.checkDamage(baseDamage * random.uniform(0.8, 1.2))