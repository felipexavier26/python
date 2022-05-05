from turtle import st


nome = str(input("Digite o seu o nome completo? "))
print("Analisando seu nome....")
print("O seu nome em minúsculo é {}".format(nome.lower())) #lower e letra em minúsculo
print("O seu nome em maiúscula é {}".format(nome.upper())) # upper e letra em maiuscula
print("O seu nome tem ao todo {} letras".format(len(nome))) # len é a quantidade de lebra digitada
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))
