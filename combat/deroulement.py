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

    def is_combat_over(self):
        return self.player.hp <= 0 or self.enemy.hp <= 0

    def get_winner(self):
        if self.player.hp > 0:
            return self.player
        elif self.enemy.hp > 0:
            return self.enemy
        return None

    def execute_action(self, action):
        result = action.execute()
        self.next_turn()
        return result