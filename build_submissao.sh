#!/bin/bash

# PLANEJADOR="/tmp/dir/software/planners/downward/fast-downward.py --alias lama-first --plan-file /tmp/output_a190030879.sas"
# PLANEJADOR="/home/prof/ribas/planners/downward/fast-downward.py --alias lama-first --plan-file sas_plan"
PLANEJADOR="/tmp/dir/software/planners/madagascar/M -o /tmp/output_a190030879.sas"
# PLANEJADOR="/home/prof/ribas/planners/madagascar/M -o sas_plan"

ARQUIVO_DOMINIO="/dominios/lightsout_madagascar.pddl"
DOMINIO=`cat $ARQUIVO_DOMINIO`

LOCAL_PROBLEMA="/tmp/problema.pddl"
LOCAL_DOMINIO="/tmp/domain.pddl"
LOCAL_SAS_PLAN="/tmp/output_a190030879.sas"

cat lightsout.py | sed -e "s@<alterar_planejador>@$PLANEJADOR@g" \
                       -e "s@<alterar_local_problema>@$LOCAL_PROBLEMA@g" \
                       -e "s@<alterar_local_dominio>@$LOCAL_DOMINIO@g" \
                       -e "s@<alterar_local_sas_plan>@$LOCAL_SAS_PLAN@g" \
                       -e "s@<alterar_dominio>@`echo $DOMINIO`@g" > submissao.py3
