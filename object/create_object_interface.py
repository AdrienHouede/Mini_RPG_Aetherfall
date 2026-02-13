from object.armor import Armor
from object.consumable import Consumable
from object.weapon import Weapon

class FactoryObject:
    @staticmethod
    def object(name, object_type, lvl):
        if object_type == "weapon":
            return Weapon(name, lvl)
        elif object_type == "armor":
            return Armor(name, lvl)
        elif object_type == "consumable":
            return Consumable(name, lvl)
        else:
            raise ValueError("Type d'objet inconnu")