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
from pee.melhorprim.procura_custo_unif import ProcuraCustoUnif
from pee.melhorprim.procura_melhor_prim import ProcuraMelhorPrim
from pee.melhorprim.procura_sofrega import ProcuraSofrega
from pee.melhorprim.procura_aa import ProcuraAA

#Activacao
psa.iniciar("amb/amb4.das")
psa.executar(AgentePrpospector(ControloPEE(ProcuraLarg())))
