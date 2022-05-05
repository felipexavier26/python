n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
m = (n1 + n2) / 2
print("Tirando {:.1f} e {:.1f}, a média do aluno e {:.1f}: ".format(n1, n2,m))
if 7 > m >=5:
    print("Avaliação Final")
elif m < 5:
    print("Reprovado:")
elif m >= 7:
    print("Aprovado")
