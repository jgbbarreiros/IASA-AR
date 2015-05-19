from psa.util import argmax


class SelAccao(object):

    def __init__(self, mem_aprend, accoes):
        self._mem_aprend = mem_aprend
        self._accoes = accoes

    def max_accao(self, s):
        # selecionar a accao com melhor recompensa
        return argmax(self._accoes, lambda a: self._mem_aprend[(s, a)])

    def seleccionar_accao(self, s):
        abstract

    def explorar(self, s):
        abstract