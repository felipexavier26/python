#Media do aluno
n1 = float(input("Digite a primeira nota do aluno: " ))
n2 = float(input("Digite a segunda nota do aluno: "))
m = (n1 + n2) / 2
print("A nota entre {} e {} é igual a {} ".format(n1, n2, m))
if m >= 6.0:
    print("Você esta aprovado, PARABENS")
else:
    print("Estude mais REPROVADO")