from abc import ABC, abstractmethod
from enum import Enum


class TriggerTiming(Enum):
    """Defines when a status effect triggers"""
    TURN_START = "turn_start"      # Début de tour (poison)
    ON_IMPACT = "on_impact"         # À l'impact (shield absorbs damage)
    TURN_END = "turn_end"           # Fin de tour
    BEFORE_ACTION = "before_action" # Avant l'action (stun blocks action)


class Status(ABC):
    """
    Generic base class for all status effects.
    CDC-compliant: No hardcoded logic, fully polymorphic.
    """

    def __init__(self, name: str, duration: int, trigger_timing: TriggerTiming):
        """
        Args:
            name: Human-readable status name
            duration: Number of turns the status lasts (-1 for infinite)
            trigger_timing: When the status effect triggers
        """
        self.name = name
        self.duration = duration
        self.trigger_timing = trigger_timing
        self.is_expired = False

    @abstractmethod
    def apply_effect(self, target, context: dict) -> dict:
        """
        Apply the status effect. Must be implemented by subclasses.

        Args:
            target: The character/enemy affected by this status
            context: Additional context (e.g., incoming damage for shields)

        Returns:
            dict: Result of applying the effect (for combat log)
        """
        pass

    def tick_duration(self):
        """Decrement duration after each turn"""
        if self.duration > 0:
            self.duration -= 1
            if self.duration == 0:
                self.is_expired = True

    def should_expire(self) -> bool:
        """Check if status should be removed"""
        return self.is_expired

    def on_remove(self, target) -> dict:
        """
        Optional cleanup when status is removed.
        Override in subclasses if needed.
        """
        return {
            "action": "status_removed",
            "status": self.name,
            "target": target.__class__.__name__
        }
