v1 = float(input("digite a velocidade do veiculo? "))
if v1 > 80:
    print("MULTADO! Você excedeu o limite de velocidade de 80km!")
    multa =  (v1-80) * 7
    print("Você deve pagar uma multa de {}".format(multa))
else:
    print("Tenha um bom dia! dirija com segurança!")
