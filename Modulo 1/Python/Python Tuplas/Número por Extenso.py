numero = int(input('Digite um número de 0 a 20: '))
nome = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while numero not in range(0, 20 + 1):
    numero = int(input('Tente novamente. Digite um número de 0 a 20: '))

print(f'O número digitado por extenso fica: {nome[numero]}')