from math import radians, sin, cos, tan
import math
angulo = float(input("Digite o angulo que voce deseja: "))
seno = math.sin(radians(angulo))
print("O Ãngulo de {} tem o SENO de {}".format(angulo,seno))
cosseno = cos(radians(angulo))
print("O ãngulo de {} tem o COSSENO de {:.2f}".format(angulo,cosseno))
tangente = tan(radians(angulo))
print("O angulo de {} tem a TANGENTE de {:.2f}".format(angulo,tangente))

 