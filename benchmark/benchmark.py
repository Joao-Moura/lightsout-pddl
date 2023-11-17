import os
import time
import sys

import subprocess

from glob import glob

from validador import valida_jogadas


def remove_extra_files(files):
    for arquivos_extras in files:
        try:
            os.remove(arquivos_extras)
        except FileNotFoundError:
            continue


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <planner_args>")
        exit(1)

    subprocess.run(['./build_submissao_chococino.sh'] + sys.argv[1:])
    mapas = glob('benchmark/mapas/*')
    mapas.sort()

    tempo_total_final = 0

    for mapa in mapas:
        remove_extra_files(['sas_plan', 'problema.pddl', 'domain.pddl'])
        f = open(mapa, 'r')

        initial_time = time.time()
        retorno = subprocess.run(
            ['python3', 'submissao.py3'], stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        tempo_total = time.time() - initial_time

        f.close()

        retorno_stdout = retorno.stdout.decode('utf-8')

        tempo_total_final += tempo_total
        qtd_passos = len(retorno_stdout.split(';'))
        vitoria = 'Sucesso' if valida_jogadas(retorno_stdout, mapa) else 'Derrota'

        retorno_falha = f'\n|_ Plano encontrado: [{retorno_stdout[:-1]}]' if vitoria == 'Derrota' else ''
        print(f'Executado mapa {mapa} com {qtd_passos} passos em {tempo_total}s [{vitoria}]' + retorno_falha)

        remove_extra_files(['problema.pddl', 'domain.pddl'])

    print(f'Tempo total final: {tempo_total_final}s')

if __name__ == "__main__":
    main()
