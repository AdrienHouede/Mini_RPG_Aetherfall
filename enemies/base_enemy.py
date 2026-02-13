from combat.coef_damage import CoefDamage

class BaseEnemy:
    def __init__(self, lvl):
        self.pv = 100 * lvl
        self.defense = 10 * lvl
        self.attack = 10 * lvl
        self.speed = 1 * lvl
        self.crititcal = 1 * lvl

    def attack_hero(self, player):
         damage = CoefDamage.calculDamage(self.attack - player.defense)
         return player.pv - damage
