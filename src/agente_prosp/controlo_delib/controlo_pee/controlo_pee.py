from controlo_delib.controlo_delib import ControloDelib
from mod_prob.problema_plan import ProblemaPlan
from mod_prob.operador_mover import OperadorMover
from psa.util import argmin
from psa.actuador import MOVER
import psa


class ControloPEE(ControloDelib):

    def __init__(self, mec_proc):
        super(ControloPEE, self).__init__() # ControloDelib.__init__(self)
        self._mec_proc = mec_proc
        self._operadores = [OperadorMover(self._crencas, accao) for accao in self._crencas.accoes()]
        self._plano = []

    def _reconsiderar(self):
        # talvez reconsiderar algo mais
        return not self._plano

    def _planear(self):
        if self._intencoes:
            # perceber que estado final tenho que passar
            problema = ProblemaPlan(self._crencas.estado(), self._intencoes[0], self._operadores)
            solucao = self._mec_proc.procurar(problema)
            self._plano = [no.operador for no in solucao[1:]]

    def _executar(self):
        # percorrer a solucao
        if self._plano:
            psa.vismod.elementos(self._crencas._imagem)
            psa.vismod.plano(self._crencas.estado(), self._plano)
            return MOVER(self._plano.pop(0).ang)

    def _seleccionar_opcoes(self):
        # escolher o melhor desejo
        return [argmin(self._desejos, lambda desejo: self._crencas.custo_accao(self._crencas.estado(), None, desejo))]