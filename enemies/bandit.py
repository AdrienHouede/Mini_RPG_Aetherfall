from enemies.base_enemy import BaseEnemy
from combat.coef_damage import CoefDamage

class Bandit(BaseEnemy):
    def __init__(self, lvl):
        super().__init__(lvl)

    def steal(self, player):
        damage = CoefDamage.calculDamage(self.attack * 0.5 - player.defense)
        return player.pv - damage