print('{:=^60}'.format(" Loja Xavier "))
preço = float(input("Preço da compras: R$ "))
print('''FORMA DE PAGAMENTOS
[ 1 ] á vista denhiero/cheque
[ 2 ] á vista cartão débito
[ 3 ] 2X no cartão de credito de crédito
[ 4 ] 3x ou mais no cartão de crédito ''')
opção = int(input("Qual é a opção de pagamento? "))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preço,total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preço,total))
elif opção == 3:
    total = preço 
    parcela = total / 2
    print("Sua compra será parcelado em 2x de R${:.2f}".format(parcela))
elif opção == 4:
    total = preço
    total = preço + (preço * 20 / 100)
    totalparcela = int(input("Quantas parcela deseja?"))
    parcela = total / totalparcela
    print("Sua compra seráparcelado em {}x de R${:.2f} COM JUROS ".format(totalparcela, parcela))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preço,total))

