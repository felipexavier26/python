Listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    Listanum.append(int(input(f"Digite um valor para a Posição {c}: ")))
    if c == 0:
        maior = menor = Listanum[c]
    else:
        if Listanum[c] > maior:
            maior = Listanum[c]
            if Listanum[c] < menor:
                menor = Listanum[c]
print("=-" *30)
print(f"Você digitou os valores {Listanum}: ")
print(f"O maior valor digitado foi {maior} nas posições ", end='')
for i, v in enumerate(Listanum):
    if c == maior:
        print(f"{i}...", end='')
print()
print(f"O menor valor digitado foi {menor} nas posições ", end='')
for i, v in enumerate(Listanum):
    if v == menor:
        print(f"{i}... ", end='')
print()