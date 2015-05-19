from sel_accao import SelAccao

class SelAccaoEGreedy(SelAccao):

    def __init__(self, mem_aprend, accoes, epsilon):
        super(SelAccaoEGreedy, self).__init__(mem_aprend, accoes)
        self._epsilon = epsilon

    def seleccionar_accao(self, s):
        pass

    def explorar(self, s):
        pass