peso = float(input("Digite seu peso? (Kg) "))
altura = float(input("Digite sua altura? (m) "))
imc = peso/(altura ** 2 )
print("O IMC da pessoa é de {:.1f}".format(imc))
if imc <= 18.5:
    print("Abaixo do peso:")
elif imc > 18.5 and  imc <= 25:
    print("Peso Ideal!")
elif imc > 25 and imc <=30:
    print("Sobrepeso")
elif imc > 30 and imc <= 40:
    print("Obesidade:")
else:
    print("Obesidade mórbida")