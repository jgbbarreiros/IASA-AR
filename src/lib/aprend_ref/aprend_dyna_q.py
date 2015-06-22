from aprend_q import AprendQ
from random import choice


class AprendDynaQ(AprendQ):

    def __init__(self, mem_aprend, sel_accao, alfa, gama, num_sim):
        super(AprendDynaQ, self).__init__(mem_aprend, sel_accao, alfa, gama)
        self._iniciar_modelo()
        self._num_sim = num_sim

    def _iniciar_modelo(self):
        self._T = dict() # T(s, a) transicao (estado)
        self._R = dict() # R(s, a) recompensa local

    def aprender(self, s, a, r, sn):
        super(AprendDynaQ, self).aprender(s, a, r, sn)
        self._actualizar_modelo(s, a, r, sn)
        self._simular()

    def _simular(self):
        for i in range(self._num_sim):
            chave_aleatoria = choice(self._T.keys())
            s = chave_aleatoria[0]
            a = chave_aleatoria[1]
            r = self._R[chave_aleatoria]
            sn = self._T[chave_aleatoria]
            super(AprendDynaQ, self).aprender(s, a, r, sn)

    def _actualizar_modelo(self, s, a ,r ,sn):
        # actualizar T(s, a) e R(s, a)
        self._T[(s, a)] = sn
        self._R[(s, a)] = r
