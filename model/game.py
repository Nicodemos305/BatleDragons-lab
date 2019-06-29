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
        if hp1 <= 0:
            print 'Voce tombou'
        if hp2 <= 0:
            print 'O inimigo tombou'

    def show_hero_damage(self, name_hero_atack, damage, name_hero_damage):
        print 'O heroi ' + name_hero_atack + ' atacou o heroi ' + name_hero_damage
        print 'O heroi ' + name_hero_damage + ' recebeu ' + str(damage) + ' de dano'