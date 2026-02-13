class Competence:
    def __init__(self, caster, target, skill_method, status_to_apply=None):
        self.caster = caster
        self.target = target
        self.skill_method = skill_method
        self.status_to_apply = status_to_apply

    def execute(self):
        damage = self.skill_method(self.target)

        result = {
            "damage": damage,
            "caster": self.caster.__class__.__name__,
            "target": self.target.__class__.__name__,
            "skill": self.skill_method.__name__
        }

        if self.status_to_apply:
            status_result = self.target.add_status(self.status_to_apply)
            result["status_applied"] = status_result

        return result