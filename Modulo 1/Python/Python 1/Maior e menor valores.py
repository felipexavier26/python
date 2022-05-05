a = int(input("Digte o primeiro numero? "))
b = int(input("Digte o segundo numero? "))
c = int(input("Digte o terceiro numero? "))
if a<b and a<c:
    menor = a
if b<1 and b<c:
    menor = b
if c<a and c<b:
    menor = c
print("O menor valor digitado é {}".format(menor))
