from object.armor import Armor
from object.consumable import Consumable
from object.weapon import Weapon

class FactoryObject:
    @staticmethod
    def object(object_type, lvl):
        if object_type == "weapon":
            return Weapon(lvl)
        elif object_type == "armor":
            return Armor(lvl)
        elif object_type == "consumable":
            return Consumable(lvl)
        else:
            raise ValueError("Type d'objet inconnu")