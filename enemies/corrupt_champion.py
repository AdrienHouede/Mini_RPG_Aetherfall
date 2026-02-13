from enemies.base_enemy import BaseEnemy
from combat.coef_damage import CoefDamage

class CorruptChampion(BaseEnemy):
    def __init__(self, lvl):
        super().__init__(lvl)

    def annihilation(self, player):
        damage = CoefDamage.calcul_damage(self.attack * 2)
        player.hp -= damage
        return damage