times = ('São Paulo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'Flamengo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print("-=" *30)
print("Lista de times do Brasileirão: ".format(times))
print("-=" *30)
print(f"Os 5 primeiros são{times[0:5]}: ")
print("-=" *30)
print(f"Os 4 ultimos são {times[-4:]}")
print("-=" *30)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=" *30)
print(f"O Goiás esta na {times.index('Goiás')} posição")
    