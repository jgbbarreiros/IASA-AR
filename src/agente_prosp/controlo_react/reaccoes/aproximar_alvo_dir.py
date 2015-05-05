from ecr.reaccao import Reaccao
from ecr.resposta import Resposta


class AproximarAlvoDir(Reaccao):

    def __init__(self, dir):
        self._dir = dir

    def detectar_estimulo(self, percepcao):
        if percepcao[self._dir].alvo:
            return percepcao[self._dir].distancia

    def gerar_resposta(self, estimulo):
        return Resposta((1, self._dir), 1/(1+estimulo))