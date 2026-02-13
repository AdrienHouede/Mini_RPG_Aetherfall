from enemies.base_enemy import BaseEnemy

class Squeleton(BaseEnemy):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.defense = self.defense + 20
