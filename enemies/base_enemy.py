from combat.coef_damage import CoefDamage

class BaseEnemy:
    def __init__(self, lvl):
        self.hp = 100 * lvl
        self.defense = 10 * lvl
        self.attack = 10 * lvl
        self.speed = 1 * lvl
        self.critical = 0.05 * lvl

    def attack_hero(self, player):
        damage = CoefDamage.calcul_damage(self.attack - player.defense)
        player.hp -= damage
        return damage
