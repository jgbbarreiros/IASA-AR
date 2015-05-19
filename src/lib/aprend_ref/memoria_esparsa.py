from memoria_aprend import MemoriaAprend


class MemoriaEsparsa(MemoriaAprend):

    def __init__(self, valor_omissao=0.0):
        self._memoria = dict()
        self._valor_omissao = valor_omissao

    def __getitem__(self, key):
        return self._memoria.get(key, self._valor_omissao)

    def __setitem__(self, key, value):
        self._memoria[key] = value

