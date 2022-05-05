frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) # Juntar as palavras
inverso = ''
for letra in range(len(junto) - 1 , -1, -1 ): # inverso de letra
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palindromo: ")
else:
    print("O termo  não é um palindromo: ")
    

