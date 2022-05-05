print("GERADOR DE PA! ") 
print("-=" * 10)
primeiro  = int(input("Primeiro termo: "))
razão = int(input('Razão da PA! '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <=  10:
        print("{} > ".format(termo), end= " ")
        termo += razão 
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termo você quer mostra  a mais? "))
print("Processando finalizada com {} termo mostrado! ".format(total))
print("FIM")