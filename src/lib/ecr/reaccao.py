from esquema_comport import EsquemaComport

class Reaccao(EsquemaComport):

    def detectar_estimulo(self, percepcao):
        abstract

    def gerar_resposta(self, estimulo):
        abstract

    def activar(self, percepcao):
        estimulo = self.detectar_estimulo(percepcao)
        if estimulo is not None and estimulo != False:
            resposta = self.gerar_resposta(estimulo)
            return resposta