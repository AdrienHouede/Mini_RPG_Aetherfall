class Item:
    def __init__(self, name, item_type, value):
        self.name = name
        self.type = item_type
        self.value = value

class Potion(Item):
    def __init__(self, value=30):
        super().__init__("Potion", "heal", value)

class MegaPotion(Item):
    def __init__(self, value=50):
        super().__init__("Mega Potion", "heal", value)

class AttackBoost(Item):
    def __init__(self, value=5):
        super().__init__("Attack Boost", "attack", value)

class DefenseBoost(Item):
    def __init__(self, value=5):
        super().__init__("Defense Boost", "defense", value)

class SpeedBoost(Item):
    def __init__(self, value=3):
        super().__init__("Speed Boost", "speed", value)
