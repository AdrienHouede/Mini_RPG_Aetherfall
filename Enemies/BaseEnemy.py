class BaseEnemy:
    def __init__(self, pv, strength, defense, attack, speed, critical):
        self.pv = pv
        self.strenght = strength
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.crititcal = critical

    def AttackHero(self, player):
        player.pv - self.attack
