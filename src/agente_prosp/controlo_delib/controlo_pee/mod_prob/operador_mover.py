from pee.modprob.operador import Operador


class OperadorMover(Operador):

    def __init__(self, modelo_mundo, angulo):
        self._modelo_mundo = modelo_mundo
        self._angulo = angulo

    @property
    def ang(self):
        return self._angulo

    def aplicar(self, estado):
        transicoes = self._modelo_mundo.simular_accao(estado, self._angulo)
        if transicoes:
            p, estado_suc = transicoes[0]
            return estado_suc

    def custo(self, estado, estado_suc):
        return self._modelo_mundo.custo_accao(estado, self._angulo, estado_suc)

