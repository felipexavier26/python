from pickle import TRUE


n = s = 0
while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    s += n
print("A soma é {}".format(s))