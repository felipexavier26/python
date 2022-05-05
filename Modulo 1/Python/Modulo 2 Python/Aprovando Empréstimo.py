casa = float(input("Valor da casa: R$ "))
salario = float(input("Digite seu salario: R$ "))
anos = int(input("Quantos anos de financiamento? "))
prestação = casa / (anos * 12)
minino = salario * 30 / 100 # 30% do salario
print("Para pagar uma casa de R${:.2f} em {} anos".format(casa,anos), end='')
print(" A prestação será de R$ {}".format(prestação))
if prestação <= minino:
    print("Financiamento APROVADO!")
else:
    print("Financiamento NEGADO!")
