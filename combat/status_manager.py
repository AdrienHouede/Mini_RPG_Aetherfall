from typing import List, Dict
from combat.status import Status, TriggerTiming


class StatusManager:
    """
    Manages status effects for characters/enemies.
    CDC-compliant: Generic status handling, no hardcoded types.
    """

    def __init__(self):
        self.statuses: List[Status] = []

    def add_status(self, status: Status) -> Dict:
        """Add a new status effect"""
        self.statuses.append(status)
        return {
            "action": "status_applied",
            "status": status.name,
            "duration": status.duration
        }

    def remove_status(self, status: Status, target) -> Dict:
        """Remove a status and trigger cleanup"""
        if status in self.statuses:
            self.statuses.remove(status)
            return status.on_remove(target)
        return {}

    def process_statuses(self, target, trigger: TriggerTiming, context: dict = None) -> List[Dict]:
        """
        Process all statuses matching the given trigger timing.
        CDC-compliant: No if/else for status types, pure polymorphism.

        Args:
            target: The character/enemy with statuses
            trigger: When this is being called (TURN_START, ON_IMPACT, etc.)
            context: Additional data (e.g., incoming_damage for shields)

        Returns:
            List of result dictionaries for combat log
        """
        if context is None:
            context = {}

        results = []
        statuses_to_remove = []

        # Process all statuses matching this trigger
        for status in self.statuses:
            if status.trigger_timing == trigger:
                result = status.apply_effect(target, context)
                results.append(result)

                # Check for expiration after applying
                if status.should_expire():
                    statuses_to_remove.append(status)

        # Remove expired statuses
        for status in statuses_to_remove:
            removal_result = self.remove_status(status, target)
            results.append(removal_result)

        return results

    def tick_all_statuses(self, target) -> List[Dict]:
        """
        Decrement duration on all statuses and remove expired ones.
        Call this at end of turn.
        """
        results = []
        statuses_to_remove = []

        for status in self.statuses:
            status.tick_duration()
            if status.should_expire():
                statuses_to_remove.append(status)

        for status in statuses_to_remove:
            removal_result = self.remove_status(status, target)
            results.append(removal_result)

        return results

    def has_status_by_name(self, status_name: str) -> bool:
        """Check if a specific status is active"""
        return any(s.name == status_name for s in self.statuses)

    def get_active_statuses(self) -> List[Status]:
        """Get all currently active statuses"""
        return self.statuses.copy()

    def is_stunned(self) -> bool:
        """Convenience method to check if stunned (blocks actions)"""
        return any(
            s.trigger_timing == TriggerTiming.BEFORE_ACTION
            for s in self.statuses
        )
