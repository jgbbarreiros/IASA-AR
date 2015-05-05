from ecr.reaccao import Reaccao
from psa.actuador import ESQ, FRT
from ecr.resposta import Resposta


class EvitarObst(Reaccao):

    def detectar_estimulo(self, percepcao):
        estimulo = percepcao[FRT].contacto and percepcao[FRT].obstaculo
        return estimulo

    def gerar_resposta(self, estimulo):
        return Resposta((0, ESQ))