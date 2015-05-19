from esquema_coord import EsquemaCoord


class Hierarquia(EsquemaCoord):

    def seleccionar_resposta(self, respostas):
        return respostas[0]