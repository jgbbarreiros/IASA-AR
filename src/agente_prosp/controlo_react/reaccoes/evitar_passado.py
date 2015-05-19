from ecr.reaccao import Reaccao
from explorar import Explorar

class EvitarPassado(Reaccao):

    def __init__(self):
        self._memoria = []
        self._memoria_max = 20
        self._explorar = Explorar()

    def detectar_estimulo(self, percepcao):
        return percepcao.posicao

    def gerar_resposta(self, estimulo):
        recordar = self._recordar(estimulo)
        self._memorizar(estimulo)
        self._esquecer()
        if recordar:
            return self._explorar.activar()

    def _recordar(self, posicao):
        return posicao in self._memoria

    def _esquecer(self):
        if len(self._memoria) > self._memoria_max:
            self._memoria.pop(0)

    def _memorizar(self, posicao):
        self._memoria.append(posicao)