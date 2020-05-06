def metade(preco=0, formata=False):
    res = preco / 2
    return res if formata is False else moeda(res)


def dobro(preco=0, formata=False):
    res = preco * 2
    return res if formata is False else moeda(res)


def aumentar(preco=0, taxa=0, formata=False):
    res = preco + (preco * taxa / 100)
    return res if formata is False else moeda(res)


def reduzir(preco=0, taxa=0, formata=False):
    res = preco - (preco * taxa / 100)
    return res if not formata else moeda(res)


def moeda(preco=0, moeda='€', formata=False):
    return f'{moeda}{preco:>.2f}.'.replace('.', ',')


def resumo(preco=0, taxa=10, taxa1=5):
    print(f'=' * 30)
    print(f'    RESUMO DO VALOR'.center(30))
    print(f'=' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{taxa1}% de redução: \t\t{reduzir(preco, taxa1, True)}') # \t =tabulações pa ajustar valor
    return resumo
