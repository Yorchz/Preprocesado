import numpy as np

class Escalar:

    def __init__(self):
        self.Xmax = 0
        self.Xmin = 0
        self.max = 0
        self.min = 0
        self.condicional = 0
        self.maximos_minimos = []

    def ajustar(self, x, miin=-1, maax=1):

        if isinstance(x[0], (int, float, np.int, np.float)):
            self.ajustar_list(x)
            self.ajustar_min_mix(miin, maax)
            self.condicional = 1
        else:
            self.ajustar_l_list(x)
            self.ajustar_min_mix(miin, maax)

    def ajustar_list(self, x):
        self.Xmax = max(x)
        self.Xmin = min(x)

    def ajustar_l_list(self, y):

        for i in range(len(y)):
            self.maximos_minimos.append([max(y[i]), min(y[i])])

    def ajustar_min_mix(self, miin, maax):
        self.max = maax
        self.min = miin

    def max_minus_min(self):
        return self.max - self.min

    def Xmax_minus_Xmin(self):
        return self.Xmax - self.Xmin

    def min_mult_Xmax(self):
        return self.min * self.Xmax

    def max_mult_Xmin(self):
        return self.max * self.Xmin

    def transformar(self, x):
        if self.condicional == 1:
            return self.no_matriz_transformar(x)
        else:
            return self.matriz_tranformar(x)

    def transformar_inv(self, x):
        if self.condicional == 1:
            return self.no_matriz_transformar_inv(x)
        else:
            return self.matriz_tranformar_inv(x)

    def matriz_tranformar(self, x):
        listy = []
        for i in range(len(x)):
            self.sacar_max_min(self.maximos_minimos[i])
            listy.append(self.no_matriz_transformar(x[i]))
        return listy

    def no_matriz_transformar(self, x):
        return [((self.max_minus_min() * i) + (self.min_mult_Xmax() - self.max_mult_Xmin())) /
                self.Xmax_minus_Xmin() for i in x]

    def matriz_tranformar_inv(self, x):
        list = []
        for i in range(len(x)):
            self.sacar_max_min(self.maximos_minimos[i])
            list.append(self.no_matriz_transformar_inv(x[i]))
        return list

    def no_matriz_transformar_inv(self, x):
        return [(i * self.Xmax_minus_Xmin() - self.min_mult_Xmax() +
                 self.max_mult_Xmin()) / self.max_minus_min() for i in x]

    def sacar_max_min(self, maximos_minimos):
        self.Xmax = maximos_minimos[0]
        self.Xmin = maximos_minimos[1]
