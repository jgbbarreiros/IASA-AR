from sel_accao import SelAccao
from random import random
from random import choice


class SelAccaoEGreedy(SelAccao):

    def __init__(self, mem_aprend, accoes, epsilon):
        super(SelAccaoEGreedy, self).__init__(mem_aprend, accoes)
        self._epsilon = epsilon

    def seleccionar_accao(self, s):
        if random() < self._epsilon:
            return self.explorar(s)
        else:
            return self.max_accao(s)

    def explorar(self, s):
        return choice(self._accoes)