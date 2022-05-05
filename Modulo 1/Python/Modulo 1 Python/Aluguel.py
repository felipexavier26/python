#Fazer o calculo de um veiculo alugado#
dias = float(input("Quantos dias alugado? "))
km = float(input("Quantos KM rodados? "))
pago = (dias * 60) + (km * 0.15)
print("O total a ser pago {}".format(pago)) 