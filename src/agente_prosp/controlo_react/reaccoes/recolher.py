from ecr.comportamento import Comportamento
from ecr.coord.hierarquia import Hierarquia
from evitar_obst import EvitarObst
from explorar import Explorar
from contornar_obst import ContornarObst
from aproximar_alvo import AproximarAlvo

class Recolher(Comportamento):

    def __init__(self):
        super(Recolher, self).__init__(Hierarquia(), [AproximarAlvo(), EvitarObst(), ContornarObst(), Explorar()])