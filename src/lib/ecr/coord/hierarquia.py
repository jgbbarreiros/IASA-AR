from ecr.coord.esquema_coord import EsquemaCoord


class Hierarquia(EsquemaCoord):

    def selecionar_resposta(self, respostas):
        return respostas[0]