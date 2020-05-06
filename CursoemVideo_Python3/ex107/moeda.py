def metade(preco):
    res = preco / 2
    print(f'~' * 30)
    return res


def dobro(preco):
    res = preco * 2
    print(f'~' * 30)
    return res


def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    print(f'~' * 30)
    return res


def reduzir(preco, taxa):
    res = preco - (preco * taxa/100)
    print(f'~' * 30)
    return res
