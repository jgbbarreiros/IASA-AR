from controlo import Controlo
from reaccoes.recolher import Recolher


class ControloReact(Controlo):

    def __init__(self):
        self._reacao = Recolher()

    def processar(self, percepcao):
        resposta = self._reacao.activar(percepcao)
        return resposta.accao