#soma, substração, multiplicação, e divisão#
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
soma = a + b
substracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print("--" *12)
print("O resultado da soma é: {soma}\nO resultado da sub é: {substracao}\nO resultado da multi é: {multiplicacao}\nO resultado da divisão é: {divisao}\nÉ o resto do resto é: {resto}\n ".format(soma=soma, substracao=substracao, multiplicacao=multiplicacao, divisao=divisao, resto=resto)) 
print("--" *12)