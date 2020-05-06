def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[0;31mERRO! \"{n}\" é inválido.')
        else:
            ok = True
            return float(n)
