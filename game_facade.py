from personnages.guerrier import Guerrier
from personnages.mage import Mage
from personnages.voleur import Voleur
from object.create_object_interface import FactoryObject

class GameFacade:
    def __init__(self):
        self.player = None
        self.running = True

    def start_game(self):
        print("Bienvenue dans Mini RPG Aetherfall !")
        self.choose_character()
        self.setup_starting_gear()
        self.game_loop()

    def choose_character(self):
        print("\nChoisissez votre classe :")
        print("1. Guerrier")
        print("2. Mage")
        print("3. Voleur")
        
        while True:
            choice = input("Votre choix (1-3) : ")
            if choice == "1":
                self.player = Guerrier()
                print("Vous avez choisi : Guerrier")
                break
            elif choice == "2":
                self.player = Mage()
                print("Vous avez choisi : Mage")
                break
            elif choice == "3":
                self.player = Voleur()
                print("Vous avez choisi : Voleur")
                break
            else:
                print("Choix invalide.")

    def setup_starting_gear(self):
        baton = FactoryObject.object("Baton", "weapon", 1)
        tunique = FactoryObject.object("Tunique", "armor", 1)

        print("\nVous recevez votre équipement de base...")
        self.player.inventory.add(baton)
        self.player.inventory.add(tunique)

        self.player.inventory.equip(baton)
        self.player.inventory.equip(tunique)

    def game_loop(self):
        while self.running:
            print("\n--- Menu Principal ---")
            print("1. Afficher les statistiques")
            print("2. Gestion de l'inventaire")
            print("3. Quitter")

            choice = input("Choix : ")

            if choice == "1":
                self.show_stats()
            elif choice == "2":
                self.manage_inventory()
            elif choice == "3":
                print("Au revoir !")
                self.running = False
            else:
                print("Option invalide.")

    def show_stats(self):
        p = self.player
        inv = p.inventory
        w_name = inv.equipped_weapon.name if inv.equipped_weapon else "Aucune"
        a_name = inv.equipped_armor.name if inv.equipped_armor else "Aucune"

        print(f"\n--- Statistiques de {p.__class__.__name__} ---")
        print(f"PV: {p.hp}")
        print(f"Attaque: {p.attack} (Arme: {w_name})")
        print(f"Défense: {p.defense} (Armure: {a_name})")
        print(f"Vitesse: {p.speed}")
        print(f"Critique: {p.critical}")

    def manage_inventory(self):
        inv = self.player.inventory
        print("\n--- Inventaire ---")
        
        # Objets équipés
        print(f"Arme équipée : {inv.equipped_weapon.name if inv.equipped_weapon else 'Aucune'}")
        print(f"Armure équipée : {inv.equipped_armor.name if inv.equipped_armor else 'Aucune'}")

        # Objets dans le sac
        print("\nObjets dans le sac :")
        if not inv.items:
            print(" (Vide)")
        else:
            for i, item in enumerate(inv.items):
                stats = ""
                if item.type == "weapon":
                    stats = f"(Attaque: {item.attack})"
                elif item.type == "armor":
                    stats = f"(Défense: {item.defense})"
                elif item.type == "heal":
                    stats = f"(Soin: {item.value})"
                print(f" {i + 1}. {item.name} {stats} [{item.type}]")

        print("\nActions :")
        print("E. Équiper un objet")
        print("D. Déséquiper un objet")
        print("R. Retour")

        action = input("Choix : ").upper()

        if action == "E":
            if not inv.items:
                print("Rien à équiper.")
                return
            try:
                idx = int(input("Numéro de l'objet à équiper : ")) - 1
                if 0 <= idx < len(inv.items):
                    item = inv.items[idx]
                    inv.equip(item)
                else:
                    print("Numéro invalide.")
            except ValueError:
                print("Entrée invalide.")

        elif action == "D":
            print("1. Déséquiper Arme")
            print("2. Déséquiper Armure")
            choix_d = input("Choix : ")
            if choix_d == "1":
                inv.unequip("weapon")
            elif choix_d == "2":
                inv.unequip("armor")
            else:
                print("Annulé.")
        
        elif action == "R":
            return
        else:
            print("Action inconnue.")
