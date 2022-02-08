class Escalar:

    def __init__(self):

        self.Xmax = 0
        self.Xmin = 0
        self.max = 0
        self.min = 0
        self.xPrima = []
        self.xPrimaInv = []

    def ajustar(self, x, miin=-1, maax=1):

        self.Xmax = max(x)
        self.Xmin = min(x)
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

        for i in range(len(x)):
            self.xPrima.append(round((self.max_minus_min() * x[i]) / self.Xmax_minus_Xmin() +
                                     ((self.min_mult_Xmax() - self.max_mult_Xmin()) / self.Xmax_minus_Xmin()), 2))

        return self.xPrima

    def transformar_inv(self, x):

        for i in range(len(x)):
            self.xPrimaInv.append(round((x[i] * self.Xmax_minus_Xmin() - self.min_mult_Xmax() +
                                         self.max_mult_Xmin()) / self.max_minus_min(), 2))
        return self.xPrimaInv
