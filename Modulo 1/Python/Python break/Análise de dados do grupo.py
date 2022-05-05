tot18 = totH = totM20 = 0
print("-" *30)
print("CADASTRRE UMA PESSOA ")
print("-" *30)
'Até que o break seja executado loop'
while True:
    "Digitar a idade"
    idade = int(input("Idade: "))
    sexo = " "
    "Se não for M/F"
    while sexo not in "MF":
        "Escolher o sexo M/F"
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    " Se a idade for mais do que 18 anos"
    if idade >= 18:
        tot18 +=1
    "Se o sexo for masculino"
    if sexo == "M":
        totH += 1
    "Se o sexo for Feminino e igual a 20 anos"
    if sexo == "F" and idade < 20:
        totM20 += 1
    'Ler a respostas'     
    resp = " "
    while resp not in "SN":
          resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
          "Se não digitar N vai ficar perguntado sempre"
    if resp == "N":
        break
print("Total de pessoas com mais de 18 anos: ".format(tot18))
print("Ao todo temos {} homens cadastrados: ".format(totH))
print("E temos {} mulheres com menos de 20 anos: ".format(totM20))