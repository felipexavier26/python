#Calcular um aumento ao funcionario#
salario = float(input("Qual é o salario do funcionario? R$"))
novo = salario + (salario * 15 / 100)
print("Um funcionario que ganhava R$ {}, passaram a ganhar R${}".format(salario, novo))