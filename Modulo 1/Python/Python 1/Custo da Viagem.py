distancia = float(input("Informe a distancia de viagem? "))
print("Você esta preste a comecar uma viagem {}".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
    print("É o preco da sua passagem sera de {:.2f}".format(preco))
