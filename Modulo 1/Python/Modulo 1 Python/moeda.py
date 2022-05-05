#Calcular o valor da moeda em dola#
print("Digite o valor para ser convertido R$")
n =  float(input("R$"))
print(f'R${n} = U${n/5.52 :.2f}')
print(f"R${n} = €{n/6.10 :.2f}")
print(f"R${n} = ¥{n/ 0.47 :.2f}")