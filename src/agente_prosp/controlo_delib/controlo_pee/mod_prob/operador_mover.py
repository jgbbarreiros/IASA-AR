from pee.modprob.operador import Operador


class OperadorMover(Operador):

    def __init__(self, modelo_mundo, ang):
        self._modelo_mundo = modelo_mundo
        self._ang = ang

    def aplicar(self, estado):
        transicoes = self._modelo_mundo.simular_accao(estado, self._ang)
        if transicoes:
            p, estado_suc = transicoes[0]
            return estado_suc

    def custo(self, estado, estado_suc):
        return self._modelo_mundo.custo_accao(estado, self._ang, estado_suc)

