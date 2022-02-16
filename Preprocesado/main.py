from Preprocesado.Escalar import Escalar
import numpy as np

prueba = np.array([[5, 2, 6, 9, 3], [6, 7, 6, 4, 1], [8, 4, 4, 7, 0]])

escalar = Escalar()

escalar.ajustar(prueba)
print(escalar.transformar(prueba))
print(escalar.transformar_inv(escalar.transformar(prueba)))


