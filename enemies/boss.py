from enemies.base_enemy import BaseEnemy
from combat.coef_damage import CoefDamage

class BossP1(BaseEnemy, ):
    def __init__(self, lvl):
        super().__init__(lvl)

    def kameamea(self, player):
        damage = CoefDamage.calcul_damage(self.attack * 2)
        player.defense -= 10
        player.hp -= damage
        return damage