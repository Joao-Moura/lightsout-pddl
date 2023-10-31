from pprint import pprint


def inverte(mapa, x, y):
    if (x >= len(mapa) or x < 0) or (y >= len(mapa) or y < 0):
        return

    local = mapa[x][y]
    alteracao = 'd' if local.lower() == 'l' else 'l'
    mapa[x][y] = alteracao.upper() if local.isupper() else alteracao


def apertar(mapa, x, y):
    inverte(mapa, x - 1, y)
    inverte(mapa, x + 1, y)
    inverte(mapa, x, y - 1)
    inverte(mapa, x, y + 1)

    if mapa[x][y].isupper():
        inverte(mapa, x, y)


def main():
    mapa = []
    with open('input', 'r') as f:
        for linha in f.readlines():
            mapa.append([*linha[:-1]])

    pprint(f'----------------==[Mapa Original]==----------------')
    pprint(mapa)
    print()

    jogadas = 0
    with open('passos', 'r') as f:
        for instrucao in f.readline().split(';'):
            apertar(mapa, int(instrucao[1]), int(instrucao[4]))
            jogadas += 1

    pprint(f'----------------==[Jogada Final ({jogadas})]==----------------')
    pprint(mapa)

    resultado = 'VITORIA :>'
    for linha in range(len(mapa)):
        for coluna in range(len(mapa)):
            if mapa[linha][coluna] in ['l', 'L']:
                resultado = 'TEM LAMPADA LIGADA, QUE ABALO :<'
                break

    print(f'\n{resultado} - mapa {len(mapa)}x{len(mapa)}')


if __name__ == "__main__":
    main()
