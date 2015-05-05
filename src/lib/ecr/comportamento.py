from esquema_comport import EsquemaComport


class Comportamento(EsquemaComport):

    def __init__(self, reaccoes, esquema_coord):
        self._reaccoes = reaccoes
        self._esquema_coord = esquema_coord

    def activar(self, percepcao):
        respostas = []
        for reaccao in self._reaccoes:
            resposta = reaccao.activar()
            if resposta is not None:
                respostas.append(resposta)
        if respostas:
            resposta_selecionada = self._esquema_coord.selecionar_resposta(respostas)
            return resposta_selecionada