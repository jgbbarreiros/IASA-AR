from aprend_q import AprendQ

class AprendDynaQ(AprendQ):

    def __init__(self, mem_aprend, sel_accao, alfa, gama, num_sim):
        super(AprendDynaQ, self).__init__(mem_aprend, sel_accao, alfa, gama)
        self._T = None
        self._R = None
        self._num_sim = num_sim
        pass

    def _simular(self):
        pass