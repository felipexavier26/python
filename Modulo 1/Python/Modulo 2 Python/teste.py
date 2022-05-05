nome = str(input("Digite seu nome? "))
if nome == 'felipe':
    print("Que nome bonito!".format(nome))
    print("Tenha um Bom Dia!")
elif nome == 'Pedro' or nome == 'Maria ' or nome == 'Paulo':
    print("Seu nome e bem popular no brasil!")
elif nome in 'Ana Claudia Jessica Rebeca':
    print('Que Belo nome feminino {}!'.format(nome))
    print("Tenha um Bom Dia!")