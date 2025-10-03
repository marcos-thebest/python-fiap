import random

#mini jogo de rpg
print("Bem-vindo ao mini jogo de RPG!")
print("Tem um Orc")
vida_do_orc = 10
velocidade_do_orc = 4
opcao_escolhida_pelo_usuario = int(input("digite 1 para bater 2 para fugir: "))

if(opcao_escolhida_pelo_usuario == 1):
   porrada = random.randint(1, 10)
   vida_orc = vida_do_orc - porrada
   if(vida_orc == 0):
       print("O Orc morreu")
