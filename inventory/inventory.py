class InventoryFacade:
    def __init__(self, character):
        self.character = character
        self.items = []
        self.max_size = 10
        self.equipped_weapon = None
        self.equipped_armor = None

    def add(self, item):
        if len(self.items) >= self.max_size:
            print("Inventaire plein")
            return False
        self.items.append(item)
        print(f"Ajouté {item.name}")
        return True

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Retiré {item.name}")
            return True
        print("Objet non trouvé")
        return False

    def equip(self, item):
        if item not in self.items:
             print("L'objet n'est pas dans l'inventaire")
             return False

        if item.type == "weapon":
            self.items.remove(item)
            if self.equipped_weapon:
                self.items.append(self.equipped_weapon)
                print(f"Déséquipé {self.equipped_weapon.name}")
                self.character.attack -= self.equipped_weapon.attack
            
            self.equipped_weapon = item
            self.character.attack += item.attack
            print(f"Équipé {item.name}")
            return True

        elif item.type == "armor":
             self.items.remove(item)
             if self.equipped_armor:
                 self.items.append(self.equipped_armor)
                 print(f"Déséquipé {self.equipped_armor.name}")
                 self.character.defense -= self.equipped_armor.defense
            
             self.equipped_armor = item
             self.character.defense += item.defense
             print(f"Équipé {item.name}")
             return True
        
        print("Cet objet ne peut pas être équipé")
        return False

    def unequip(self, type_item):
        if type_item == "weapon" and self.equipped_weapon:
            self.items.append(self.equipped_weapon)
            self.character.attack -= self.equipped_weapon.attack
            print(f"Déséquipé {self.equipped_weapon.name}")
            self.equipped_weapon = None
            return True
        elif type_item == "armor" and self.equipped_armor:
            self.items.append(self.equipped_armor)
            self.character.defense -= self.equipped_armor.defense
            print(f"Déséquipé {self.equipped_armor.name}")
            self.equipped_armor = None
            return True
        
        print(f"Rien à déséquiper pour {type_item}")
        return False
