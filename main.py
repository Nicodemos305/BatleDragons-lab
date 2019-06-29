from model import dragon
from model import game

if __name__ == '__main__':

    instance = game.Game()
    player1 = instance.begin()
    print '------------------------------'
    enemy = dragon.Dragon().born_dragon('enemy', "3")
    print 'Sua batalha vai comecar, voce enfrentara um inimigo'
    print enemy.name + ' entrou no combate'
while player1.hp > 0:

    damage1 = instance.roll_d6(player1.atk)
    damage2 = instance.roll_d6(enemy.atk)

    print '------------------------------'
    print 'Sua vez de atacar ' + player1.name
    instance.show_hero_damage(player1.name, damage2, enemy.name)
    print '------------------------------'
    print 'Sua vez de atacar ' + enemy.name
    instance.show_hero_damage(enemy.name, damage1, player1.name)
    print '------------------------------'

    player1.hp = player1.hp - damage1
    enemy.hp = enemy.hp - damage2
    print 'voce recebeu um ataque, seu hp e ' + str(player1.hp)
    print 'O hp do inimigo e ' + str(enemy.hp)
    print '------------------------------'
    instance.who_is_chanpion(player1.hp, enemy.hp)