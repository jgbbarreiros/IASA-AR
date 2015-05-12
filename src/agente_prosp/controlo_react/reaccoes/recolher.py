from ecr.comportamento import Comportamento
from ecr.coord.hierarquia import Hierarquia
from aproximar_alvo import AproximarAlvo
from evitar_obst import EvitarObst
from contornar_obst import ContornarObst
from seguir_pot import SeguirPot
from evitar_passado import EvitarPassado
from explorar import Explorar


class Recolher(Comportamento):

    def __init__(self):
        super(Recolher, self).__init__(Hierarquia(),
            [AproximarAlvo(), EvitarObst(), ContornarObst(), EvitarPassado(), SeguirPot(), Explorar()])