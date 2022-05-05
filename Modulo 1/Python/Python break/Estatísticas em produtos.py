'variavel total' 'variavel totmil' 'variavel menor' 'variavel contrador'
total = totmil = menor = cont = 0
'variavel produto mais barato'
barato = ' '
'Até que o break seja executado loop'
while True:
    'digitar o produto'
    produto = str(input("Nome do Produto: "))
    "digitar o valor"
    preco = float(input("Preço R$ "))
    "Meu contrador vale mais 1"
    cont += 1
    "Valor total da compra"
    total += preco
    "Produto que custa mais de mil reais "
    if preco > 1000:
        totmil +=1 
    "se o contrador for o primeiro numero"     
    if cont == 1 or preco < menor:
        "o menor para ser o preço"    
        menor  = preco
        "Quando o contrador for igual a 1 o barato vai receber produto"
        barato = produto    
    'Ler a respostas'   
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    "Se não digitar N vai ficar perguntado sempre"
    if resp == "N":
        break
print("{:-^40}".format("FIM DO PROGRAMA "))
print("O total da compra foi R$ {} ".format(total))
print("Temos o produto {} que custando mais de R$1000.00 ".format(totmil))
print("O produto mais barato foi {} custa R$ {} ".format(barato, menor))