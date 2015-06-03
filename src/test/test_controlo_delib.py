# import sys
# sys.path.append("../agente_prosp")
# sys.path.append("../lib")

import psa

# Definicao de Agente Prospector
from agente_prospector import AgentePrpospector

# Definicao de Controlo Reactivo
from controlo_delib.controlo_pdm.controlo_pdm import ControloPDM

#Activacao
psa.iniciar("amb/amb4.das")
psa.executar(AgentePrpospector(ControloPDM()))
