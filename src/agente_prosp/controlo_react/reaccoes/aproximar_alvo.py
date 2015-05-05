from ecr.comportamento import Comportamento
from ecr.coord.prioridade import Prioridade
from psa.actuador import ESQ, DIR, FRT
from aproximar_alvo_dir import AproximarAlvoDir


class AproximarAlvo(Comportamento):

     def __init__(self):
        super(AproximarAlvo, self).__init__(Prioridade(),
            [AproximarAlvoDir(ESQ), AproximarAlvoDir(DIR), AproximarAlvoDir(FRT)])