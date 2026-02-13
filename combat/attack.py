import random
from combat.status import ON_IMPACT


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

        impact_results = self.target.process_statuses(
            ON_IMPACT,
            context={"incoming_damage": damage}
        )

        final_damage = damage
        for result in impact_results:
            if result.get("action") == "shield_absorbed":
                final_damage = result.get("remaining_damage", damage)
                break

        self.target.hp -= final_damage

        return {
            "damage": damage,
            "final_damage": final_damage,
            "critical": is_critical,
            "attacker": self.attacker.__class__.__name__,
            "target": self.target.__class__.__name__,
            "impact_effects": impact_results
        }