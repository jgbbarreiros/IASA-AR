from ecr.reaccao import Reaccao
from ecr.resposta import Resposta

class SeguirPotDir(Reaccao):

    def __init__(self, dir):
        self._dir = dir

    def detectar_estimulo(self, percepcao):
        if  percepcao[self._dir].pot_alvo > 0:
            return percepcao[self._dir].pot_alvo

    def gerar_resposta(self, estimulo):
        return Resposta((1, self._dir), estimulo)