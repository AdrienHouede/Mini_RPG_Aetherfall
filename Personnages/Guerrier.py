from Personnage import Personnages

class Guerrier(Personnages):
    def __init__(self, pv, force, defense, attaque, vitesse, critique):
        super().__init__(pv, force, defense, attaque, vitesse, critique)
        self.attaque = 1.5
        self.defense = 10
        self.vitesse = 5
        self.critique = 0.1

    def coupPuissant(self, cible):
        degats = self.force * self.attaque * 2 - cible.defense
        self.checkDamage(degats)
        cible.pv -= degats
        return degats
    
    def chargeHeroique(self, cible):
        degats = self.force * self.attaque * 1.5 - cible.defense
        self.checkDamage(degats)
        cible.pv -= degats
        return degats