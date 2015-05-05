from ecr.comportamento import Comportamento
from ecr.coord.prioridade import Prioridade
from psa.actuador import ESQ, DIR, FRT
from seguir_pot_dir import SeguirPotDir


class SeguirPot(Comportamento):

    def __init__(self):
        super(SeguirPot, self).__init__(Prioridade(),
            [SeguirPotDir(ESQ), SeguirPotDir(DIR), SeguirPotDir(FRT)])