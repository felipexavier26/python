#Comprimento em metro#
n = float(input('Digite um comprimento em metro: '))
print('O comprimento escolhido é {}m, este equivale: \n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(n, n/1000, n/100, n/10, n*10, n*100, n*1000))