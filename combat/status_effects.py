from combat.status import Status, TriggerTiming


class PoisonStatus(Status):
    """
    Poison (Empoisonnement): Fixed HP loss at turn start.
    Effective against high-HP enemies.
    """

    def __init__(self, damage_per_turn: int, duration: int = 3):
        super().__init__(
            name="Poison",
            duration=duration,
            trigger_timing=TriggerTiming.TURN_START
        )
        self.damage_per_turn = damage_per_turn

    def apply_effect(self, target, context: dict) -> dict:
        """Apply poison damage at turn start"""
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
    """
    Shield (Bouclier): Absorbs damage before HP is affected.
    Expires when shield points depleted OR duration expires.
    """

    def __init__(self, shield_points: int, duration: int = 3):
        super().__init__(
            name="Shield",
            duration=duration,
            trigger_timing=TriggerTiming.ON_IMPACT
        )
        self.shield_points = shield_points
        self.initial_shield_points = shield_points

    def apply_effect(self, target, context: dict) -> dict:
        """
        Absorb incoming damage.
        Context must contain 'incoming_damage' key.
        """
        incoming_damage = context.get("incoming_damage", 0)

        if incoming_damage <= 0:
            return {"action": "shield_no_damage"}

        absorbed = min(self.shield_points, incoming_damage)
        self.shield_points -= absorbed
        remaining_damage = incoming_damage - absorbed

        # Shield broken
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

    def on_remove(self, target) -> dict:
        result = super().on_remove(target)
        result["shield_absorbed_total"] = self.initial_shield_points - self.shield_points
        return result


class StunStatus(Status):
    """
    Stun (Étourdissement): Target skips their next turn completely.
    Duration typically 1 turn.
    """

    def __init__(self, duration: int = 1):
        super().__init__(
            name="Stun",
            duration=duration,
            trigger_timing=TriggerTiming.BEFORE_ACTION
        )

    def apply_effect(self, target, context: dict) -> dict:
        """
        Prevent action from executing.
        Returns indication that action should be blocked.
        """
        return {
            "action": "stunned",
            "status": self.name,
            "target": target.__class__.__name__,
            "action_blocked": True,
            "remaining_duration": self.duration
        }
