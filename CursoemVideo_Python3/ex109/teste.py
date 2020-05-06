from ex109 import moeda

p = float(input('\033[0;32mDigite um preço €: \033[m'))
print(f'A metade de {moeda.moeda(p)} é {(moeda.metade(p, True))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(p, 13, True)}')
