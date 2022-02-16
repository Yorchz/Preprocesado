from Preprocesado.Escalar import Escalar
import numpy as np

vector0 = np.array([5, 2, 6, 9, 3])
vector = np.array([[1, 7, 5, 2], [9, 6, 3, 4], [2, 1, 5, 6], [7, 8, 4, 6]])

escalar = Escalar()

escalar.ajustar(vector0)
print(escalar.transformar(vector0))
print(escalar.transformar_inv(escalar.transformar(vector0)))


