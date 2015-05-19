from controlo import Controlo
from aprend_ref.sel_accao_e_greedy import SelAccaoEGreedy
from aprend_ref.memoria_esparsa import MemoriaEsparsa
from aprend_ref.aprend_dyna_q import AprendDynaQ
from psa.actuador import MOVER
from psa.util import dirmov
from psa.util import dist
import psa


class ControloAprendRef(Controlo):

    def __init__(self):
        self._r_max = 100.
        self._s = None
        self._a = None
        self._accoes = dirmov()
        self._mem_aprend = MemoriaEsparsa()
        self._mec_sel_accao = SelAccaoEGreedy(self._mem_aprend, self._accoes, 0.01)
        self._mec_aprend = AprendDynaQ(self._mem_aprend, self._mec_sel_accao, 0.5, 0.95, 100)

    def processar(self, percepcao):
        sn = percepcao.posicao # observar proximo estado
        if self._a is not None: # ver ser pode aprender na memoria se houve accao anterior
            ref = self.reforco(percepcao, self._s, sn) # gerrar reforco
            self._mec_aprend.aprender(self._s, self._a, ref, sn) # activar o mecanismo de aprend e aprender
            psa.vismod.accaovalordir(self._mem_aprend._memoria, self._accoes)

        an = self._mec_sel_accao.seleccionar_accao(sn) # gerar a proxima accao
        # guardar memoria
        self._s = sn
        self._a = an
        return MOVER(an) # MOVER(ang)

    def reforco(self, percepcao, s, sn):
        ref = -dist(s, sn)
        if percepcao.alvo:
            ref += self._r_max
        if percepcao.colisao:
            ref -= self._r_max
        return ref # double
