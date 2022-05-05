nome = input("Digite seu nome completo! ")
print('Seja bem-vindo', nome)

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar 
    [ 2 ] Multiplicar 
    [ 3 ] maior 
    [ 4 ] Novos números 
    [ 5 ] Sair do programa ''')
    opção = int(input(">>>>> Qual é a sua opção! "))
   
   # somar os valores
    if opção == 1:
        soma = n1 + n2
        print("A soma  entre {} e {} é {}".format(n1, n2, soma))
    
    #Multiplicar os valores
    elif opção == 2:
        produto = n1 * n2
        print("O resultado entre {} e {} é ".format(n1, n2 , produto))
        
    # Mostrar o maior valor            
    elif opção == 3:
        if n1 > n2:
            maior = n2
        else:
            maior = n2
        print("Entre {} e {} o maior é {}".format(n1, n2, maior))
        
     #informar os valores na tela   
    elif opção == 4:
        print("Informar os números novamente! ")
        n1 = int(input("Primeiro valor! "))
        n2 = int(input("Segunto valor! "))
        
    elif opção == 5:
        print("Finalizando.....")
    else:
         print("Opção inválida. Tente novamente! ")
    print(' =-=' * 10)   
print("Fim do prohrama! Volte sempre!! ", nome)
        
        
        
        
        

