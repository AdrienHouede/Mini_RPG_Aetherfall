from personnages.guerrier import Guerrier
from personnages.mage import Mage
from personnages.voleur import Voleur
from enemies.wolf import Wolf
from enemies.bandit import Bandit
from combat.action_combat import ActionCombat
from combat.item import Potion, AttackBoost

def combat_example():
    player = Guerrier()
    enemy = Wolf(lvl=1)

    combat = ActionCombat(player, enemy)

    print(f"Combat: {player.__class__.__name__} vs {enemy.__class__.__name__}")
    print(f"Player HP: {player.hp} | Enemy HP: {enemy.hp}")
    print("-" * 50)

    turn = 1
    while not combat.is_combat_over():
        current_fighter = combat.get_current_fighter()
        print(f"\nTour {turn} - {current_fighter.__class__.__name__} agit")

        if current_fighter == player:
            if turn == 1:
                result = combat.attack(player, enemy)
                print(f"Attaque normale: {result['damage']:.2f} dégâts {'CRITIQUE!' if result.get('critical') else ''}")
            elif turn == 3:
                result = combat.use_skill(player, enemy, player.powerful_strike)
                print(f"Compétence {result['skill']}: {result['damage']:.2f} dégâts")
            elif turn == 5:
                potion = Potion()
                result = combat.use_item(player, potion)
                print(f"Utilise {result['item']}: +{result['change']:.2f} {result['stat']}")
            else:
                result = combat.attack(player, enemy)
                print(f"Attaque: {result['damage']:.2f} dégâts")
        else:
            result = combat.attack(enemy, player)
            print(f"Attaque: {result['damage']:.2f} dégâts")

        print(f"Player HP: {player.hp:.2f} | Enemy HP: {enemy.hp:.2f}")
        turn += 1

    winner = combat.get_winner()
    print("\n" + "=" * 50)
    print(f"Combat terminé! Vainqueur: {winner.__class__.__name__}")
    print(f"HP restant: {winner.hp:.2f}")

if __name__ == "__main__":
    combat_example()
