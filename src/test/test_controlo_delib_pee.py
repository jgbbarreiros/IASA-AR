# import sys
# sys.path.append("../agente_prosp")
# sys.path.append("../lib")

import psa

# Definicao de Agente Prospector
from agente_prospector import AgentePrpospector

# Definicao de Controlo PEE
from controlo_delib.controlo_pee.controlo_pee import ControloPEE

# Definicao de Mecanismos Procura
from pee.prof.procura_prof import ProcuraProf
from pee.larg.procura_larg import ProcuraLarg
from pee.melhorprim.procura_custo_unif import ProcuraCustoUnif # 1
from pee.melhorprim.procura_melhor_prim import ProcuraMelhorPrim
from pee.melhorprim.procura_sofrega import ProcuraSofrega # 2
from pee.melhorprim.procura_aa import ProcuraAA # 3

#Activacao
psa.iniciar("amb/amb4.das")#, dinamb=0.1)
print ProcuraAA
psa.executar(AgentePrpospector(ControloPEE(ProcuraAA())))
