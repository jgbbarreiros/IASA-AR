from controlo_delib import ModeloMundo
from math import pi
from psa.util import mover


class ModeloMundoND(ModeloMundo):

    def simular_accao(self, s, a):
        pass
        # sn = mover(s, a)
        # sn2 = mover(s, a-(pi/4))
        # sn3 = mover(s, a+(pi/4))
        # if sn in self._estados:
        #     return [(.8, sn), (.1, sn2), (.1, sn3)]
        # else:
        #     return [(1, s)]

        # prob_accoes = [(.8, a), (.1, a-(pi/4)), (.1, a+(pi/4))]
        # transicoes =[(prob_accao[0], mover(prob_accao[1])) for prob_accao in prob_accoes]
        # for transicao in transicoes:
        #     if transicao[1] not in self._estados:
        #         transicoes[transicao][(1, s)]
        # return transicoes
