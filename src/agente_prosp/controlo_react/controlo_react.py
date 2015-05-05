from controlo import Controlo
from reaccoes.explorar import Explorar

class ControloReact(Controlo):

    def __init__(self):
        self._reacao = Explorar()

    def processar(self, percepcao):
        resposta = self._reacao.activar(percepcao)
        return resposta.accao