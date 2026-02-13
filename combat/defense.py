class Defense:
    def __init__(self, defender, boost_value=5):
        self.defender = defender
        self.boost_value = boost_value
        self.original_defense = defender.defense

    def execute(self):
        self.defender.defense += self.boost_value
        return {
            "defender": self.defender.__class__.__name__,
            "boost": self.boost_value,
            "new_defense": self.defender.defense
        }

    def reset(self):
        self.defender.defense = self.original_defense