from ex111.utilidadesCeV import moeda
from ex111.utilidadesCeV.dado import leiaDinheiro

p = leiaDinheiro('\033[7;31mDigite um preço €:\033[m ')
moeda.resumo(p, 10, 5)
