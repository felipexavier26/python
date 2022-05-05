#Começa com \033 [
#style /0 none/1 bold/4 underline/7 negativo/
#text /30 Branco/31 vermelho/ 32 verde/33 amarelo/34 azul/35 roxo/36 lilas/37 cinza
# back /40 Branco/41 vermelho/ 42 verde/43 amarelo/44 azul/45 roxo/46 lilas/47 cinza

a = 3
b = 5
print("Os valor são \033[1;32;40m{} e \033[4;32;45m{}".format(a,b))
