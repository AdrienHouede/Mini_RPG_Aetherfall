from combat.deroulement import Deroulement
from combat.attack import Attack
from combat.defense import Defense
from combat.competence import Competence
from combat.object import ObjectAction

class ActionCombat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.deroulement = Deroulement(player, enemy)
        self.combat_log = []

    def attack(self, attacker, target):
        action = Attack(attacker, target)
        result = self.deroulement.execute_action(action)
        self.combat_log.append(result)
        return result

    def defend(self, defender):
        action = Defense(defender)
        result = self.deroulement.execute_action(action)
        self.combat_log.append(result)
        return result

    def use_skill(self, caster, target, skill_method):
        action = Competence(caster, target, skill_method)
        result = self.deroulement.execute_action(action)
        self.combat_log.append(result)
        return result

    def use_item(self, user, item):
        action = ObjectAction(user, item)
        result = self.deroulement.execute_action(action)
        self.combat_log.append(result)
        return result

    def is_combat_over(self):
        return self.deroulement.is_combat_over()

    def get_winner(self):
        return self.deroulement.get_winner()

    def get_current_fighter(self):
        return self.deroulement.get_current_fighter()

    def get_combat_log(self):
        return self.combat_log