from combat.status import TURN_START, BEFORE_ACTION, TURN_END


class Deroulement:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn_order = self.determine_turn_order()
        self.current_turn = 0

    def determine_turn_order(self):
        if self.player.speed >= self.enemy.speed:
            return [self.player, self.enemy]
        else:
            return [self.enemy, self.player]

    def get_current_fighter(self):
        return self.turn_order[self.current_turn % 2]

    def next_turn(self):
        self.current_turn += 1

        next_fighter = self.get_current_fighter()
        turn_start_results = next_fighter.process_statuses(TURN_START)
        return turn_start_results

    def is_combat_over(self):
        return self.player.hp <= 0 or self.enemy.hp <= 0

    def get_winner(self):
        if self.player.hp > 0:
            return self.player
        elif self.enemy.hp > 0:
            return self.enemy
        return None

    def execute_action(self, action):
        current_fighter = self.get_current_fighter()

        before_action_results = current_fighter.process_statuses(BEFORE_ACTION)

        action_blocked = False
        for result in before_action_results:
            if result.get("action_blocked", False):
                action_blocked = True
                break

        if action_blocked:
            self.next_turn()
            return {
                "action": "action_blocked",
                "fighter": current_fighter.__class__.__name__,
                "status_results": before_action_results
            }

        result = action.execute()

        turn_end_results = current_fighter.process_statuses(TURN_END)

        tick_results = current_fighter.tick_statuses()

        result["status_effects"] = {
            "before_action": before_action_results,
            "turn_end": turn_end_results,
            "duration_ticks": tick_results
        }

        self.next_turn()
        return result