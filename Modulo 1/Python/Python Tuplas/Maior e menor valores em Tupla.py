# random é geradores de números
# gera números reais
from random import randint
números = randint (0, 10), randint (0, 10), randint (0, 10), randint (0, 10), randint (0, 10)
print("Os valores sorteado foram: ", end= '')
for n in números:
    print(f" {n} ", end= ' ')
# sortear o maior valor
print(f"\nO maior valor sorteado foi {max(números)}")
# Sortear o menor valor
print(f"O menor valor sorteado foi {min(números)}")