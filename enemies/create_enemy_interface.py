from enemies.squeleton import Squeleton
from enemies.wolf import Wolf


class FactoryEnemy:
    @staticmethod
    def create_enemy(enemy_type, lvl):
        if enemy_type == "squeleton":
            return Squeleton(lvl)
        elif enemy_type == "wolf":
            return Wolf(lvl)
        else:
            raise ValueError("Type d'ennemi inconnu")