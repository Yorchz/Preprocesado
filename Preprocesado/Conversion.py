class CodificadorEtiqueta:

    def __init__(self):
        self.codificador = {}
        self.inv_codificador = {}

    def ajustar(self, y):

        resultado = {}
        key = 0

        for i in y:
            if i in resultado.keys():
                continue

            resultado[i] = key
            key = key + 1

        self.codificador = resultado
        self.inv_codificador = {v: k for k, v in resultado.items()}
        return self.inv_codificador

    def transformar(self, y):

        transformada = []

        for i in y:

            if i in self.codificador.keys():
                transformada.append(self.codificador[i])
            else:
                raise ValueError(y[i], "No se ha encontrado el valor")

        return transformada

    def transformar_inv(self, y):

        transformada_inv = []

        for i in y:

            if i in self.inv_codificador.keys():
                transformada_inv.append(self.inv_codificador[i])
            else:
                raise ValueError(y[i], "No se ha encontrado el valor")

        return transformada_inv
