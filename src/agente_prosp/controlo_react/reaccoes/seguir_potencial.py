from ecr.comportamento import Comportamento
from psa.actuador import ESQ, DIR, FRT
from seguir_potencial_dir import SeguirPotencialDir
from ecr.coord.prioridade import Prioridade

class SeguirPotencial(Comportamento):

    def __init__(self):
        super(SeguirPotencial, self).__init__(Prioridade(),
            [SeguirPotencialDir(ESQ), SeguirPotencialDir(DIR), SeguirPotencialDir(FRT)])