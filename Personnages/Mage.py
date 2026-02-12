from Personnage import Personnages

class Mage(Personnages):
    def __init__(self, pv, force, defense, attaque, vitesse, critique):
        super().__init__(pv, force, defense, attaque, vitesse, critique)
        self.attaque = 2

    def bouleFeu(self, cible):
        degats = self.force * self.attaque * 1.5 - cible.defense
        self.checkDamage(degats)
        cible.pv -= degats
        return degats
    
    def bouclierArcanique(self, valeur):
        self.defense += valeur