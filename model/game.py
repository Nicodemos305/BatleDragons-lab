import random
from model import dragon
class Game:

    def __init__(self):
        print("*****************************************")
        print("****************BATLE DRAGON*************")
        print("*****************************************")

    def begin(self):
        print("Seja bem vindo ao mundo dos Dragoes, escolha um dragao para criar.")
        print("-------------------------------------------------------------------")
        print("1 - Dragao de Gelo, poderoso dragao glacial. E uma especie que evoluiu dos dragoes marinhos das areas glaciais.")
        print("2 - Dragao de Fogo, poderoso dragao de fogo. Essa especie vive dentro de um vulcao.")
        print("3 - Dragao de Comun, um poderoso dragao. Essa especie vive em montanhas e florestas.")
        print("-------------------------------------------------------------------")
        dragon_choice = raw_input()
        print 'Digite o nome de seu personagem'
        name = raw_input()
        player1 = dragon.Dragon().born_dragon(name, dragon_choice)
        return player1

    def roll_d6(self, value):
        return random.randint(1, value)

    def who_is_chanpion(self, hp1, hp2):
        if hp1 < hp2 and hp1 <= 0:
            print 'Voce tombou'
        elif hp2 < hp1 and hp2 <= 0:
            print 'O inimigo tombou'

    def show_hero_damage(self, name_hero_atack, damage, name_hero_damage):
        print 'O heroi {} atacou o heroi {}'.format(name_hero_atack, name_hero_damage)
        print 'O heroi {} recebeu {} de dano'.format(name_hero_damage, str(damage))

    def born_enemy(self):
        enemy = dragon.Dragon().born_dragon('enemy', "3")
        print enemy.name + ' entrou no combate'
        print 'Sua batalha vai comecar, voce enfrentara um inimigo'
        return enemy

    def your_phase(self, name):
        print 'Sua vez de atacar {}'.format(name)

    def calc_atack_damage(self, hp, damage):
        return hp - damage