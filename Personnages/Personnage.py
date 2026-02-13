class Personnages:
    def __init__(self, defense, attack, speed, critical):
        self.hp = 100
        self.strength = 10
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.critical = critical

    def checkDamage(self, damage):
        if damage < 0:
            damage = 0
        return damage

    def makeAttack(self, target):
        damage = self.strength * self.attack - target.defense
        damage = self.checkDamage(damage)
        target.hp -= damage
        return damage

    def useItem(self, item):
        attribute = "hp" if item.type == "heal" else item.type
        if hasattr(self, attribute):
            setattr(self, attribute, getattr(self, attribute) + item.value)

    def makeDefense(self, value):
        self.defense += value