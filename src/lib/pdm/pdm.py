from psa.util import argmax

class PDM:

    def __init__(self, modelo, delta_max, gama):
        self._modelo = modelo
        self._delta_max = delta_max
        self._gama = gama

    def utilidade(self):
        S, A= self._modelo.S, self._modelo.A
        U = {s: 0 for s in S()}
        while True:
            delta = 0
            Uant = U.copy()
            for s in S():
                U[s] = max(self.util_accao(s, a, Uant) for a in A(s))
                delta_s = abs(U[s] - Uant[s])
                delta = max(delta, delta_s)
            if delta < self._delta_max:
                break
        return U

    def politica(self, U):
        A, S = self._modelo.A, self._modelo.S
        PI = dict()
        for s in S():
            a_max = argmax(A(s), lambda a: self.util_accao(s, a, U))
            PI[s] = a_max
        return PI

    def util_accao(self, s, a, U):
        # Retorna uma probabilidade
        R, T, g = self._modelo.R, self._modelo.T, self._gama
        return sum(p*(R(s, a, sn) + g*U[sn]) for (p, sn) in T(s, a))

