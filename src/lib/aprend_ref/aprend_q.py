from aprend_ref import AprendRef

class AprendQ(AprendRef):

    def __init__(self, mem_aprend, sel_accao, alfa, gama):
        super(AprendQ, self).__init__(mem_aprend, sel_accao)
        self._alfa = alfa
        self._gama = gama

    def aprender(self, s, a, r, sn):
        # actualizar Q
        # Q(s, a) = Q(s, a) + alfa [r + gama* max(a+)Q(s', a+) - Q(s, a)]
        self._mem_aprend[(s, a)] = self._mem_aprend[(s, a)] + self._alfa * \
                                   (r + self._gama * self._sel_accao.max_accao(s) -
                                   self._mem_aprend[(s, a)]) # errado provavelmente