print("-==" *20)
print("Analisandor de Triãngulos")
print("-==" *20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segunro segmento: "))
r3 = float(input("Terxeiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print("Os segmentos acima PODEM FORMAR triãngulos")
else:
    print("Os segmentos acima NÃO PODE FORMAR triãngulos")

