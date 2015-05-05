from ecr.reaccao import Reaccao
from psa.actuador import ESQ, DIR, FRT
from ecr.resposta import Resposta

class AproximarAlvoDir(Reaccao):

    def __init__(self, dir):
        self._dir = dir

    def detectar_estimulo(self, percepcao):
        estimulo = None
        if percepcao[self._dir].alvo:
            estimulo = percepcao[self._dir].distancia
        return estimulo

    def gerar_resposta(self, estimulo):
        resposta = (1, self._dir)
        return Resposta(resposta, 1/(1+estimulo))