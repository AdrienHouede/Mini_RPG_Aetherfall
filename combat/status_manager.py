from combat.status import BEFORE_ACTION


class StatusManager:

    def __init__(self):
        self.statuses = []

    def add_status(self, status):
        self.statuses.append(status)
        return {
            "action": "status_applied",
            "status": status.name,
            "duration": status.duration
        }

    def remove_status(self, status, target):
        if status in self.statuses:
            self.statuses.remove(status)
            return status.on_remove(target)
        return {}

    def process_statuses(self, target, trigger, context=None):
        if context is None:
            context = {}

        results = []
        statuses_to_remove = []

        for status in self.statuses:
            if status.trigger_timing == trigger:
                result = status.apply_effect(target, context)
                results.append(result)

                if status.should_expire():
                    statuses_to_remove.append(status)

        for status in statuses_to_remove:
            removal_result = self.remove_status(status, target)
            results.append(removal_result)

        return results

    def tick_all_statuses(self, target):
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

    def has_status_by_name(self, status_name):
        for status in self.statuses:
            if status.name == status_name:
                return True
        return False

    def get_active_statuses(self):
        return self.statuses.copy()

    def is_stunned(self):
        for status in self.statuses:
            if status.trigger_timing == BEFORE_ACTION:
                return True
        return False
