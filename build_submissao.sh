#!/bin/bash

# PLANEJADOR="/tmp/dir/software/planners/downward/fast-downward.py --alias lama-first --plan-file /tmp/output_a190030879.sas"
PLANEJADOR="/home/prof/ribas/downward/fast-downward.py --alias lama-first"

ARQUIVO_DOMINIO="lightsout.pddl"
DOMINIO=`cat $ARQUIVO_DOMINIO`

cat lightsout.py | sed -e "s@<alterar_planejador>@$PLANEJADOR@g" \
                       -e "s@<alterar_dominio>@`echo $DOMINIO`@g" > submissao.py3
