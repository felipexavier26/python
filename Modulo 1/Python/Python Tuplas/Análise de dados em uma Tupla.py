num = int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: "))
print(f"Você digitou os valores {num}")
# Quantas vezes aparece o número 9 usando o count
print(f"O número 9 apareceu {num.count(9)} vezes ")
#Em qual posição o número 3 foi digitado
if 3 in num:
    print(f"O números 3 foi digitado {num.index(3)+1} posição")
else:
    print("O número 3 não foi digitado em nemhuma posição")
print("Os valores pares digitado foram: ", end= '')
# numeros pares
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
    