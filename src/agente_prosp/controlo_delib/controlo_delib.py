from controlo import Controlo
from modelo_mundo import ModeloMundo


class ControloDelib(Controlo):

    def __init__(self):
        self._crencas = ModeloMundo()
        self._desejos = None
        self._intencoes = None

    def processar(self, percepcao):
        self._actualizar_crencas(percepcao)
        if self._reconsiderar():
            self._deliberar()
            self._planear()
        return self._executar()

    def _actualizar_crencas(self, percepcao):
        self._crencas.actualizar(percepcao)

    def _reconsiderar(self):
        abstract

    def _deliberar(self):
        self._desejos = self._gerar_opcoes()
        if self._desejos:
            self._intencoes = self._seleccionar_opcoes()
        else:
            self._intencoes = []

    def _planear(self):
        abstract

    def _executar(self):
        abstract

    def _gerar_opcoes(self):
        return self._crencas.pos_alvos()

    def _seleccionar_opcoes(self):
        return self._desejos