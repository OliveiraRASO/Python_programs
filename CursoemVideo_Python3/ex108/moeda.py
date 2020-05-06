def metade(preco = 0):
    res = preco / 2
    print(f'~' * 30)
    return res


def dobro(preco = 0):
    res = preco * 2
    print(f'~' * 30)
    return res


def aumentar(preco = 0, taxa = 0):
    res = preco + (preco * taxa/100)
    print(f'~' * 30)
    return res


def reduzir(preco = 0, taxa = 0):
    res = preco - (preco * taxa/100)
    print(f'~' * 30)
    return res


def moeda(preco = 0, moeda = '€'):
    return f'{moeda}{preco:>.2f}.'.replace('.', ',')
