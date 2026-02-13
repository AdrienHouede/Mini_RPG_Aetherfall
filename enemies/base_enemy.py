from combat.coef_damage import CoefDamage
from combat.status_manager import StatusManager

class BaseEnemy:
    def __init__(self, lvl):
        self.hp = 100 * lvl
        self.defense = 10 * lvl
        self.attack = 10 * lvl
        self.speed = 1 * lvl
        self.critical = 0.05 * lvl
        self.status_manager = StatusManager()

    def attack_hero(self, player):
        damage = CoefDamage.calcul_damage(self.attack - player.defense)
        player.hp -= damage
        return damage

    def add_status(self, status):
        return self.status_manager.add_status(status)

    def process_statuses(self, trigger, context=None):
        return self.status_manager.process_statuses(self, trigger, context)

    def tick_statuses(self):
        return self.status_manager.tick_all_statuses(self)

    def is_stunned(self):
        return self.status_manager.is_stunned()
