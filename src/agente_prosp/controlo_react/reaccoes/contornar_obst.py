from ecr.reaccao import Reaccao
from psa.actuador import ESQ, DIR, FRT
from ecr.resposta import Resposta


class ContornarObst(Reaccao):

    def detectar_estimulo(self, percepcao):
        return percepcao[ESQ].contacto and percepcao[ESQ].obstaculo or \
               percepcao[DIR].contacto and percepcao[DIR].obstaculo

    def gerar_resposta(self, estimulo):
        return Resposta((1, FRT))

