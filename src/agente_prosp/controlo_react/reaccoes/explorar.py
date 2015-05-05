from ecr.esquema_comport import EsquemaComport
from random import choice
from psa.actuador import ESQ, DIR, FRT
from ecr.resposta import Resposta


class Explorar(EsquemaComport):

    def activar(self, percepcao):
        accao = choice([(1, ESQ), (1, FRT), (1, DIR)])
        return Resposta(accao)