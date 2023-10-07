(define (domain lightsout)
    (:types posicao)
    (:predicates (lampada-em ?x ?y - posicao)
                 (inc ?a ?b - posicao)
                 (dec ?a ?b - posicao)
                 (ta-ligada ?x ?y - posicao)
                 (ta-quebrada ?x ?y - posicao))

    (:action APERTAR
        :parameters (?x ?y - posicao)
        :precondition ()
        :effect (and
            (when (and (not (ta-quebrada ?x ?y)) (ta-ligada ?x ?y)) (not (ta-ligada ?x ?y)))
            (when (and (not (ta-quebrada ?x ?y)) (not (ta-ligada ?x ?y))) (ta-ligada ?x ?y))
            (forall
                (?w - posicao)
                (when
                    (or
                        (inc ?x ?w)
                        (inc ?y ?w)
                        (dec ?x ?w)
                        (dec ?y ?w)
                    )
                    (and
                        (when (and (lampada-em ?x ?w) (ta-ligada ?x ?w)) (not (ta-ligada ?x ?w)))
                        (when (and (lampada-em ?x ?w) (not (ta-ligada ?x ?w))) (ta-ligada ?x ?w))
                        (when (and (lampada-em ?w ?y) (ta-ligada ?w ?y)) (not (ta-ligada ?w ?y)))
                        (when (and (lampada-em ?w ?y) (not (ta-ligada ?w ?y))) (ta-ligada ?w ?y))
                    )
                )
            )
        )
    )
)
