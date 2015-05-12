from controlo import Controlo

class ControloAprendRef(Controlo):

    def __init__(self):
        self._r_max = None
        self._s = None
        self._a = None
        pass

    def processar(self, percepcao):
        pass

    def reforco(self, percepcao, s, sn):
        pass