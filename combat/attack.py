import random

class Attack:
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def execute(self):
        damage = self.attacker.attack - self.target.defense
        if damage < 0:
            damage = 0
        damage = damage * random.uniform(0.8, 1.2)
        is_critical = random.random() < self.attacker.critical
        if is_critical:
            damage *= 2
        self.target.hp -= damage
        return {
            "damage": damage,
            "critical": is_critical,
            "attacker": self.attacker.__class__.__name__,
            "target": self.target.__class__.__name__
        }