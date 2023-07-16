def dado(a):
    while True:
        b = str(input(f'{a}'))
        if b.isalpha() or b == '':
            print(f'ERRO! "{b}" não é um valor valido')
        else:
            c = b.replace(',', '.')
            return float(c)
