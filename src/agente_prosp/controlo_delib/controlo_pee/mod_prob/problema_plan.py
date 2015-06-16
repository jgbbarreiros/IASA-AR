from pee.modprob.problema import Problema
from psa import dist


class ProblemaPlan(Problema):

    def __init__(self, estado_inicial, estado_final, operadores):
        Problema.__init__(self, estado_inicial, operadores)
        self._estado_final = estado_final

    def objectivo(self, estado):
        return estado == self._estado_final

    def heuristica(self, estado):
        return dist(estado, self._estado_final)