def main():
    entradas = []
    linha = coluna = 1

    while True:
        try:
            valores = input()
            entradas += [
                f"(lampada-em x{linha} y{coluna})" +
                (f" (ta-quebrada x{linha} y{coluna})" if valor.islower() else "") +
                (f" (ta-ligada x{linha} y{coluna})" if valor.lower() == 'l' else "")
                for coluna, valor in enumerate(valores, 1)
            ]

            linha += 1
            coluna = len(valores)
        except (EOFError, KeyboardInterrupt):
            break

    incrementos = []
    for l in range(1, linha-1):
        incrementos.append(f'(inc x{l} x{l+1})')
        incrementos.append(f'(dec x{l+1} x{l})')

    for c in range(1, coluna):
        incrementos.append(f'(inc y{c} y{c+1})')
        incrementos.append(f'(dec y{c+1} y{c})')

    init = '\n'.join(entradas + incrementos)
    objects = ' '.join([f'x{l}' for l in range(1, linha)] + [f'y{c}' for c in range(1, coluna+1)]) + ' - posicao'

    goals = []
    for l in range(1, linha):
        for c in range(1, coluna+1):
            goals.append(f'(not (ta-ligada x{l} y{c}))')
    goals = '\n'.join(goals)

    # print(init)
    # print(objects)
    # print(goals)

    with open('problema.pddl', 'w') as f:
        f.write(fr"""
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


if __name__ == "__main__":
    main()
