from random import randint

computador = randint (0,5) # Faz o computador rotear um valor#
print("-=-" * 20)
print("Analisando.....")
print("-=-" *20)

jogador = int(input("Em que numero você pensou? "))#Jogador tenta adivinha
print("PROCESSANDO......")

if jogador == computador:
    print("Parabens você conseguiu me vencer ")
else:
    print("Ganhei! Eu pensei no numero {} e não no  {}".format(computador, jogador))