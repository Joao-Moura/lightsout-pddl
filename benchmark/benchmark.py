import os
import time
import sys
import shutil

import subprocess

from glob import glob


AGILE = 'agile'
SAT = 'sat'


def remove_extra_files(files):
    for arquivos_extras in files:
        try:
            os.remove(arquivos_extras)
        except FileNotFoundError:
            continue


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <track> <planner_args>")
        exit(1)

    subprocess.run(['./build_submissao_chococino.sh'] + sys.argv[2:])
    mapas = glob('benchmark/mapas/*')
    mapas.sort()

    tempo_total_final = 0

    for mapa in mapas:
        remove_extra_files(['sas_plan', 'problema.pddl', 'domain.pddl'])
        f = open(mapa, 'r')

        initial_time = time.time()
        retorno = subprocess.run(
            ['python3', 'submissao.py3'], stdin=f, capture_output=True)
        tempo_total = time.time() - initial_time

        tempo_total_final += tempo_total

        f.close()

        qtd_passos = len(retorno.stdout.decode('utf-8').split(';'))

        print(f'Executado mapa {mapa} com {qtd_passos} passos em {tempo_total}s')
        # print(f'Saida completa: {retorno.stdout.decode("utf-8")}')

        remove_extra_files(['problema.pddl', 'domain.pddl'])

    print(f'Tempo total final: {tempo_total_final}s')

if __name__ == "__main__":
    main()
