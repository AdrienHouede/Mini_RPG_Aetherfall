from enemies.base_enemy import BaseEnemy
from combat.coef_damage import CoefDamage

class BossP1(BaseEnemy, ):
    def __init__(self, lvl):
        super().__init__(lvl)

    def kameamea(self, player):
        damage = CoefDamage.calculDamage(self.attack * 2)
        player.damage -= 10
        return player.pv - damage, player.damage