from esquema_comport import EsquemaComport


class Comportamento(EsquemaComport):

    def __init__(self, esquema_coord, reaccoes):
        self._esquema_coord = esquema_coord
        self._reaccoes = reaccoes

    def activar(self, percepcao):
        respostas = []
        for reaccao in self._reaccoes:
            resposta = reaccao.activar(percepcao)
            if resposta is not None:
                respostas.append(resposta)
        if respostas:
            resposta_selecionada = self._esquema_coord.seleccionar_resposta(respostas)
            return resposta_selecionada