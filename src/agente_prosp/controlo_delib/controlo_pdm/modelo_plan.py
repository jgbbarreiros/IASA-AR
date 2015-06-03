from pdm.modeloPDM import ModeloPDM


class ModeloPlan(ModeloPDM):

    def __init__(self, modelo_mundo, objectivos, r_max):
        self._modelo_mundo = modelo_mundo
        self._objectivos = objectivos
        self._r_max = r_max

    def S(self):
        return self._modelo_mundo.estados()

    def A(self, s):
        return self._modelo_mundo.accoes()

    def T(self, s, a):
        if s in self._objectivos:
            return []
        else:
            return self._modelo_mundo.simular_accao(s, a)

    def R(self, s, a, sn):
        r = -self._modelo_mundo.custo_accao(s, a, sn)
        if sn in self._objectivos:
            r += self._r_max
        elif s == sn:
            r -= self._r_max
        return r



