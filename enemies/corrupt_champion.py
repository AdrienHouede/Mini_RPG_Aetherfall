from enemies.base_enemy import BaseEnemy
from combat.coef_damage import CoefDamage

class CorruptChampion(BaseEnemy):
    def __init__(self, lvl):
        super().__init__(lvl)

    def annihilation(self, player):
        # Ignore the player's defense for this attack
        damage = CoefDamage.calculDamage(self.attack * 2)
        return player.pv - damage