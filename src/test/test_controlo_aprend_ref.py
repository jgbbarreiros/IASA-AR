# import sys
# sys.path.append("../agente_prosp")
# sys.path.append("../lib")

import psa

# Definicao de Agente Prospector
from agente_prospector import AgentePrpospector

# Definicao de Controlo Reactivo
from controlo_aprend.controlo_aprend_ref import ControloAprendRef

#Activacao
psa.iniciar("amb/amb5.das", alvo_ini=True)
psa.executar(AgentePrpospector(ControloAprendRef()))