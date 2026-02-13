from personnages.personnage import Personnage
from combat.status_effects import ShieldStatus


class Mage(Personnage):
    def __init__(self):
        super().__init__(defense=5, attack=2, speed=7, critical=0.05)

    def fireball(self, target):
        damage = self.attack * 1.5 - target.defense
        damage = self.check_damage(damage)
        target.hp -= damage
        return damage

    def arcane_shield(self, target):
        shield = ShieldStatus(shield_points=20, duration=3)
        target.add_status(shield)
        return 0