from ecr.reaccao import Reaccao
from ecr.resposta import Resposta

class SeguirPotencialDir(Reaccao):

    def __init__(self, dir):
        self._dir = dir

    def detectar_estimulo(self, percepcao):
        estimulo = None
        if  percepcao[self._dir].pot_alvo > 0:
            estimulo = percepcao[self._dir].pot_alvo
        return estimulo

    def gerar_resposta(self, estimulo):
        resposta = (1, self._dir)
        return Resposta(resposta, estimulo)