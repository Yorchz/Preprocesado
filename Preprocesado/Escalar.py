class Escalar:

    def __init__(self):

        self.Xmax = 0
        self.Xmin = 0
        self.max = 0
        self.min = 0
        self.xPrima = []
        self.yPrima = []

    def ajustar(self, x, miin=-1, maax=1):

        self.Xmax = max(x)
        self.Xmin = min(x)
        self.max = maax
        self.min = miin


    def transformar(self, x):

        for i in range(len(x)):
            self.xPrima.append((((self.max - self.min) * x[i]) / (self.Xmax - self.Xmin)) +
                               (((self.min * self.Xmax) - (self.max * self.Xmin)) / (self.Xmax - self.Xmin)))

        return self.xPrima

    def transformar_inv(self, x):

        for i in range(len(x)):

            self.yPrima.append(((x[i]*(self.Xmax - self.Xmin)) - (self.min * self.Xmax) +
                               (self.max * self.Xmin)) / (self.max - self.min))
        return self.yPrima