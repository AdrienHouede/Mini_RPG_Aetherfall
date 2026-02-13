class Competence:
    def __init__(self, caster, target, skill_method):
        self.caster = caster
        self.target = target
        self.skill_method = skill_method

    def execute(self):
        damage = self.skill_method(self.target)
        return {
            "damage": damage,
            "caster": self.caster.__class__.__name__,
            "target": self.target.__class__.__name__,
            "skill": self.skill_method.__name__
        }