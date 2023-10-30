import re
import subprocess

PLANEJADOR = ['/home/prof/ribas/downward/fast-downward.py', '--alias', 'lama-first', '--plan-file', '/tmp/output_a190030879.sas']
# PLANEJADOR = ['/tmp/dir/software/planners/downward/fast-downward.py', '--alias', 'lama-first', '--plan-file', '/tmp/output_a190030879.sas']

def main():
    entradas = []
    linha = coluna = 0

    while True:
        try:
            valores = input()
            entradas += [
                ' '.join([
                    (f"(ta-quebrada x{linha} y{coluna})" if valor.islower() else ""),
                    (f"(ta-ligada x{linha} y{coluna})" if valor.lower() == 'l' else "")
                ]).strip()
                for coluna, valor in enumerate(valores)
                if valor in ['L', 'l', 'd']
            ]

            linha += 1
            coluna = len(valores) - 1
        except (EOFError, KeyboardInterrupt):
            break

    incrementos = []
    for l in range(0, linha-1):
        incrementos.append(f'(inc x{l} x{l+1})')
        incrementos.append(f'(inc x{l+1} x{l})')

    for c in range(0, coluna):
        incrementos.append(f'(inc y{c} y{c+1})')
        incrementos.append(f'(inc y{c+1} y{c})')

    init = '\n'.join(entradas + incrementos)
    objects = ' '.join([f'x{l}' for l in range(0, linha)]) + ' - linha ' + ' '.join([f'y{c}' for c in range(0, coluna+1)]) + ' - coluna'

    goals = []
    for l in range(0, linha):
        for c in range(0, coluna+1):
            goals.append(f'(not (ta-ligada x{l} y{c}))')
    goals = '\n'.join(goals)

    with open('/tmp/problema.pddl', 'w') as f:
        f.write(f"""
            (define (problem lightsoutproblem)
                (:domain lightsout)
                (:objects {objects})
                (:init
                    {init}
                )
                (:goal
                    (and
                        {goals}
                    )
                )
            )
            """)

    with open('/tmp/domain.pddl', 'w') as f:
        f.write("""
            (define (domain lightsout)
                (:types linha coluna - posicao)
                (:predicates (inc ?a ?b - posicao)
                             (ta-ligada ?x - linha ?y - coluna)
                             (ta-quebrada ?x - linha ?y - coluna))

                (:action APERTAR
                    :parameters (?x - linha ?y - coluna)
                    :precondition ()
                    :effect (and
                        (when (and (not (ta-quebrada ?x ?y)) (ta-ligada ?x ?y)) (not (ta-ligada ?x ?y)))
                        (when (and (not (ta-quebrada ?x ?y)) (not (ta-ligada ?x ?y))) (ta-ligada ?x ?y))
                        (forall
                            (?w - linha)
                            (when
                                (or
                                    (inc ?x ?w)
                                    (inc ?w ?x)
                                )
                                (and
                                    (when (ta-ligada ?w ?y) (not (ta-ligada ?w ?y)))
                                    (when (not (ta-ligada ?w ?y)) (ta-ligada ?w ?y))
                                )
                            )
                        )
                        (forall
                            (?w - coluna)
                            (when
                                (or
                                    (inc ?y ?w)
                                    (inc ?w ?y)
                                )
                                (and
                                    (when (ta-ligada ?x ?w) (not (ta-ligada ?x ?w)))
                                    (when (not (ta-ligada ?x ?w)) (ta-ligada ?x ?w))
                                )
                            )
                        )
                    )
                )
            )
        """)

    subprocess.run(PLANEJADOR + ['/tmp/domain.pddl', '/tmp/problema.pddl'], stdout=subprocess.DEVNULL)

    resposta = []
    with open('/tmp/output_a190030879.sas', 'r') as f:
        for line in f.readlines()[:-1]:
            x = re.findall(r'x\d{1,2}?', line)[0][1:]
            y = re.findall(r'y\d{1,2}?', line)[0][1:]
            resposta.append(f"({x}, {y})")

    print(';'.join(resposta))


if __name__ == "__main__":
    main()
