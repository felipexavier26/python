from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opçoes! 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada! "))
print('JO')
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("-="*10)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-="*11)
if computador == 0: # computador jogou PEDRA
   if jogador == 0:
       print("EMPATE")
elif jogador == 1:
    print("JOGADOR VENCEU")
elif jogador == 2:
    print("COMPUTADOR VENCE")
else:
       ("Opção invalida")
       
if computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
elif jogador == 1:
            print("Empate")
elif jogador ==2:
            print("Jogador vence")
else:
            print("Opção invalida")
            
if computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print("Jogador VENCE")
elif jogador == 1:
            print("Computador vence")
elif jogador ==2:
            print("Empate")
else:
            print("Opção invalida")
            

            
       

   
