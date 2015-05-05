from ecr.comportamento import Comportamento
from ecr.coord.hierarquia import Hierarquia
from controlo_react.reaccoes.evitar_obst import EvitarObst
from controlo_react.reaccoes.explorar import Explorar

class Recolher(Comportamento):

    def __init__(self):
        super(Recolher, self).__init__(Hierarquia(), [EvitarObst(), Explorar()])