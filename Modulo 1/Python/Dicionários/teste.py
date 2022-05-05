estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input("Unidade Fererativa: "))
    estado["Sigla"] = str(input("Sigla do Estado: "))
    #Fazer uma copia
    brasil.append(estado.copy())
for e in brasil:
     for v in e.values():
         print(v , end=" ")
     print()