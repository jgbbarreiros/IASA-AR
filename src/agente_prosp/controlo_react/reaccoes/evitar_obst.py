from psa.actuador import ESQ, DIR, FRT
from ecr.reaccao import Reaccao
from ecr.resposta import Resposta

class EvitarObst(Reaccao):

    def detectar_estimulo(self, percepcao):
        estimulo = percepcao[FRT].contacto and percepcao[FRT].obstaculo
        return estimulo

    def gerar_resposta(self, estimulo):
        resposta = (1, ESQ)
        return Resposta(resposta)