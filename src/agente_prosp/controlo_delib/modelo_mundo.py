from psa import dist
from psa.util import mover, dirmov


class ModeloMundo:

    def __init__(self):
        self._imagem = None
        self._estado = None
        self._estados = None
        self._accoes = dirmov()

    def estado(self):
        return self._estado

    def estados(self):
        return self._estados

    def accoes(self):
        return self._accoes

    def actualizar(self, percepcao):
        self._imagem = percepcao.imagem
        self._estado = percepcao.posicao
        self._estados = [pos for (pos, elem) in self._imagem.items() if elem != 'obst']

    def simular_accao(self, s, a):
        sn = mover(s, a)
        if sn in self._estados:
            return [(1, sn)]
        else:
            return [(1, s)]

    def custo_accao(self, s, a, sn):
        return dist(s, sn)

    def pos_alvos(self):
        return [pos for (pos, elem) in self._imagem.items() if elem == 'alvo'] # (x, y) [0..*]