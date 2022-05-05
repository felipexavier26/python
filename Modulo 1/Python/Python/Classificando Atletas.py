from datetime import date
atual = date.today().year
nascimento = int(input("ano de nascimento: "))
idade = atual - nascimento
print("O altera tem {} anos :".format(idade))
if idade <=9:
    print("Classificação : MIRIM")
elif idade <=14:
    print("Classificação: INFATIL")
elif  idade <=19:
    print("Classificação: JUNIOR")
elif idade <=25:
    print("Classificação: SENIOR")
else:
    print("Classificação: Master")