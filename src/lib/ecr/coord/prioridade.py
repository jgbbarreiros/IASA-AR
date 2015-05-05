from esquema_coord import EsquemaCoord


class Prioridade(EsquemaCoord):

    def selecionar_resposta(self, respostas):
        return max(respostas, key=lambda resp: resp.prioridade)