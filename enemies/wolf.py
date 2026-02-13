from enemies.base_enemy import BaseEnemy
from combat.coef_damage import CoefDamage

class Wolf(BaseEnemy):
    def __init__(self, lvl):
        super().__init__(lvl)

    def multiple_attacks(self, player):
        damage = CoefDamage.calcul_damage((self.attack * 0.8) * 3 - player.defense)
        player.hp -= damage
        return damage