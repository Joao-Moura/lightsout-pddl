(define (domain lightsout)
    (:types linha coluna - posicao)
    (:predicates (inc ?a ?b - posicao)
                 (verdadeiro)
                 (ta-ligada ?x - linha ?y - coluna)
                 (ta-quebrada ?x - linha ?y - coluna))

    (:action APERTAR
        :parameters (?x - linha ?y - coluna)
        :precondition (verdadeiro)
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
