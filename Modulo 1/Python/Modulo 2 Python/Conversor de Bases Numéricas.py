num = int(input("Digite um número inteiro? "))
print('''Escolha uma opção? :
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL 
[ 3 ] converter para HEXADECIMAL''')
opção = int(input("sua opção? "))
if opção == 1:
    print("{} e convertido para BINÁRIO é igual a  {}".format(num, bin(num)))
elif opção == 2:
    print("{} e convertido para OCTAL é igual a {}".format(num,oct(num)))
elif opção == 3:
    print("{} é convertido para HEXADECIMAL é igual a {}".format(num,hex(num)))
else:
    print("Tente novamnete! ")