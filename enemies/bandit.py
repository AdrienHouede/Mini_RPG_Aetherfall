from enemies.base_enemy import BaseEnemy
from combat.coef_damage import CoefDamage

class Bandit(BaseEnemy):
    def __init__(self, lvl):
        super().__init__(lvl)

    def steal(self, player):
        damage = CoefDamage.calcul_damage(self.attack * 0.5 - player.defense)
        player.hp -= damage
        return damage