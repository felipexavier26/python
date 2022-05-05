from ast import Num


resp  = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    Num = int(input("Digite um número: "))
    soma += Num 
    quant += 1
    if quant == 1:
        maior = menor = Num
    else:
        if Num > maior:
            maior > maior
        if Num < menor:
            menor = Num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / quant  
print("Você digitou {} números e a média foi {}!".format(quant, media))  
print("O maior Valor foi {} e o menor foi {}".format(maior, menor))