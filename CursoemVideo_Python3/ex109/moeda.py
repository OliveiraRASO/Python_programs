def metade(preco=0, formata=False):
        res = preco / 2
        print(f'~' * 30)
        return res if formata is False else moeda(res)


def dobro(preco=0, formata=False):
    res = preco * 2
    print(f'~' * 30)
    return res if formata is False else moeda(res)


def aumentar(preco=0, taxa=0, formata=False):
    res = preco + (preco * taxa/100)
    print(f'~' * 30)
    return res if formata is False else moeda(res)


def reduzir(preco=0, taxa=0, formata=False):
    res = preco - (preco * taxa/100)
    print(f'~' * 30)
    return res if not formata else moeda(res)


def moeda(preco=0, moeda='€', formata=False):
    return f'{moeda}{preco:>.2f}.'.replace('.', ',')
