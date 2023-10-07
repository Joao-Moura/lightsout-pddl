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
                (?w - posicao)
                (when
                    (or
                        (inc ?x ?w)
                        (inc ?y ?w)
                        (inc ?w ?x)
                        (inc ?w ?y)
                    )
                    (and
                        (when (ta-ligada ?x ?w) (not (ta-ligada ?x ?w)))
                        (when (not (ta-ligada ?x ?w)) (ta-ligada ?x ?w))
                        (when (ta-ligada ?w ?y) (not (ta-ligada ?w ?y)))
                        (when (not (ta-ligada ?w ?y)) (ta-ligada ?w ?y))
                    )
                )
            )
        )
    )
)
