from Personnage import Personnages
import random

class Voleur(Personnages):
    def __init__(self, pv, force, defense, attaque, vitesse, critique):
        super().__init__(pv, force, defense, attaque, vitesse, critique)
        self.critique = 0.2

    def attaqueSournoise(self, cible):
        degats = self.force * self.attaque - cible.defense
        if random.random() < self.critique:
            degats *= 2
        self.checkDamage(degats)
        cible.pv -= degats
        return degats
    
    def esquiveParfaite(self, valeur):
        self.vitesse += valeur