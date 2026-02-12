class Personnages:
    def __init__(self, pv, force, defense, attaque, vitesse, critique):
        self.pv = pv
        self.force = force
        self.defense = defense
        self.attaque = attaque
        self.vitesse = vitesse
        self.critique = critique
    
    def checkDamage(degats):
        if degats < 0 :
            degats = 0
    
    def makeAttaque(self, cible):
        degats = self.force * self.attaque - cible.defense
        self.checkDamage(degats)
        cible.pv -= degats
        return degats
    
    def utiliserObjet(self, objet):
        if objet.type == "soin":
            self.pv += objet.valeur
        elif objet.type == "force": self.force += objet.valeur
        elif objet.type == "defense": self.defense += objet.valeur
        elif objet.type == "attaque": self.attaque += objet.valeur
        elif objet.type == "vitesse": self.vitesse += objet.valeur
        elif objet.type == "critique": self.critique += objet.valeur

    def makeDefense(self, valeur):
        self.defense += valeur