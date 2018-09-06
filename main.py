class Dragon():

 def __init__(self):
    self.name = ''
    self.hp = 100
    self.atk = 15

import random

if __name__ == '__main__': 
  player1 = Dragon()
  print('Digite o nome de seu personagem')
  player1.name = raw_input()
  print('------------------------------')
  enemy = Dragon()
  enemy.name = 'enemy'
  
  print('Sua batalha vai comecar, voce enfrentara um inimigo')
  print(enemy.name+' entrou no combate')
while player1.hp > 0:
  print('Sua vez de atacar '+player1.name)
  i = random.randint(1,player1.atk)

  i2 = random.randint(1, enemy.atk)
  print('------------------------------')

  print('O inimigo '+enemy.name+' recebeu '+str(i2)+' de dano')
 
  print('o inimigo te atacou')
  print('Voce recebeu '+str(i)+' de dano')
  print('------------------------------')

  player1.hp = player1.hp - i
  enemy.hp = enemy.hp - i2
  print('voce recebeu um ataque, seu hp e '+str(player1.hp))
  print('O hp do inimigo e '+str(enemy.hp))
  print('------------------------------')

if player1.hp <= 0:
 print('Voce tombou')

if enemy.hp <= 0:
 print('O inimigo tombou')
