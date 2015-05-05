# import sys
# sys.path.append("../agente_prosp")
# sys.path.append("../lib")

import psa

# Definicao de Agente Prospector
from agente_prospector import AgentePrpospector

# Definicao de Controlo Reactivo
from controlo_react.controlo_react import ControloReact

#Activacao
psa.iniciar("amb/amb1.das")
psa.executar(AgentePrpospector(ControloReact()))