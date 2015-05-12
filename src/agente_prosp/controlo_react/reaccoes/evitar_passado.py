from ecr.reaccao import Reaccao
from explorar import Explorar

class EvitarPassado(Reaccao):

    def __init__(self):
        self.m = []
        self.m_max = 20
        self.explorar = Explorar()

    def detectar_estimulo(self, percepcao):
        return percepcao.posicao

    def gerar_resposta(self, estimulo):
        recordar = self._recordar(estimulo)
        self._memorizar(estimulo)
        self._esquecer()
        if recordar:
            print self.explorar.activar().accao
            return self.explorar.activar()

    def _recordar(self, posicao):
        return posicao in self.m

    def _esquecer(self):
        if len(self.m) > self.m_max:
            self.m.pop(0)

    def _memorizar(self, posicao):
        self.m.append(posicao)