from controlo_delib.controlo_delib import ControloDelib
from mod_prob.problema_plan import ProblemaPlan
from mod_prob.operador_mover import OperadorMover


class ControloPEE(ControloDelib):

    def __init__(self, mec_proc):
        self._mec_proc = mec_proc
        self._operadores = [OperadorMover(self._crencas, accao) for accao in self._crencas._accoes()]
        self._problema = None
        self._solucao = None

    def _reconsiderar(self):
        # TODO talvez reconsiderar algo mais
        return not self._intencoes or self._crencas.estado() in self._intencoes

    def _planear(self):
        if self._intencoes:
            # TODO perceber que estado final tenho que passar
            self._problema = ProblemaPlan(self._crencas._estado(), self._intencoes[0], self._operadores)
            self._solucao = self._mec_proc.procurar(self._problema)

    def _executar(self):
        # TODO percorrer a solucao
        return self._solucao.pop(0)