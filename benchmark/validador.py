import pprint
import sys


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


def valida_jogadas(jogadas_entrada, mapa_entrada, retornar_mapa_final=False):
    if not jogadas_entrada:
        return False

    mapa = []
    with open(mapa_entrada, 'r') as f:
        f.seek(0)
        for linha in f.readlines():
            mapa.append([*linha[:-1]])

    jogadas = 0
    for instrucao in jogadas_entrada.split(';'):
        apertar(mapa, int(instrucao[1]), int(instrucao[4]))
        jogadas += 1

    for linha in range(len(mapa)):
        for coluna in range(len(mapa)):
            if mapa[linha][coluna] in ['l', 'L']:
                if retornar_mapa_final:
                    return False, mapa
                return False
    return True


if __name__ == "__main__":
    retorno = valida_jogadas(sys.argv[1], sys.argv[2], retornar_mapa_final=True)
    if isinstance(retorno, tuple):
        print('\n'.join([''.join(r) for r in retorno[1]]))
