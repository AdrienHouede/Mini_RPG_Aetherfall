TURN_START = "turn_start"
ON_IMPACT = "on_impact"
TURN_END = "turn_end"
BEFORE_ACTION = "before_action"


class Status:

    def __init__(self, name, duration, trigger_timing):
        self.name = name
        self.duration = duration
        self.trigger_timing = trigger_timing
        self.is_expired = False

    def apply_effect(self, target, context):
        pass

    def tick_duration(self):
        if self.duration > 0:
            self.duration -= 1
            if self.duration == 0:
                self.is_expired = True

    def should_expire(self):
        return self.is_expired

    def on_remove(self, target):
        return {
            "action": "status_removed",
            "status": self.name,
            "target": target.__class__.__name__
        }
