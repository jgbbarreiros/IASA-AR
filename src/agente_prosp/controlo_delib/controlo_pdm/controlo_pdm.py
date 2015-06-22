from controlo_delib.controlo_delib import ControloDelib
from modelo_plan import ModeloPlan
from pdm.pdm import PDM
from psa.actuador import MOVER
import psa


class ControloPDM(ControloDelib):

    def __init__(self):
        super(ControloPDM, self).__init__()
        self._r_max = 100
        self._delta_max = 1
        self._gama = 0.95
        self._PI = None

    def _reconsiderar(self):
        return not self._intencoes or self._crencas.estado() in self._intencoes

    def _planear(self):
        if self._intencoes:
            modelo = ModeloPlan(self._crencas, self._intencoes, self._r_max)
            pdm = PDM(modelo, self._delta_max, self._gama)
            U = pdm.utilidade()
            self._PI = pdm.politica(U)
            psa.vismod.campo(U)
            psa.vismod.politica(self._PI)
        else:
            self._PI = None

    def _executar(self):
        if self._PI:
            accao = self._PI[self._crencas.estado()]
            if accao is not None:
                return MOVER(accao)
