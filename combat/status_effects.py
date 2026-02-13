from combat.status import Status, TURN_START, ON_IMPACT, BEFORE_ACTION


class PoisonStatus(Status):

    def __init__(self, damage_per_turn, duration=3):
        super().__init__("Poison", duration, TURN_START)
        self.damage_per_turn = damage_per_turn

    def apply_effect(self, target, context):
        target.hp -= self.damage_per_turn
        return {
            "action": "poison_damage",
            "status": self.name,
            "target": target.__class__.__name__,
            "damage": self.damage_per_turn,
            "remaining_hp": target.hp,
            "remaining_duration": self.duration
        }


class ShieldStatus(Status):

    def __init__(self, shield_points, duration=3):
        super().__init__("Shield", duration, ON_IMPACT)
        self.shield_points = shield_points
        self.initial_shield_points = shield_points

    def apply_effect(self, target, context):
        incoming_damage = context.get("incoming_damage", 0)

        if incoming_damage <= 0:
            return {"action": "shield_no_damage"}

        absorbed = min(self.shield_points, incoming_damage)
        self.shield_points -= absorbed
        remaining_damage = incoming_damage - absorbed

        if self.shield_points <= 0:
            self.is_expired = True

        return {
            "action": "shield_absorbed",
            "status": self.name,
            "target": target.__class__.__name__,
            "absorbed": absorbed,
            "remaining_damage": remaining_damage,
            "shield_remaining": self.shield_points,
            "shield_broken": self.is_expired
        }

    def on_remove(self, target):
        result = super().on_remove(target)
        result["shield_absorbed_total"] = self.initial_shield_points - self.shield_points
        return result


class StunStatus(Status):

    def __init__(self, duration=1):
        super().__init__("Stun", duration, BEFORE_ACTION)

    def apply_effect(self, target, context):
        return {
            "action": "stunned",
            "status": self.name,
            "target": target.__class__.__name__,
            "action_blocked": True,
            "remaining_duration": self.duration
        }
