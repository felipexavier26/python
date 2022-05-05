numero = int(input("Me diga um numero? "))
restaldo = numero % 2
if restaldo == 0:
    print("O numero é PAR {}".format(numero))
else:
    print("O numero é impar {}".format(numero))