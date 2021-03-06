from Preprocesado.Escalar import Escalar
from Preprocesado.Validacion_modelo import divide_entrenamiento_test
from Preprocesado.Conversion import CodificadorEtiqueta

import numpy as np

print("Función de conversión de valores:\n")

vector = ["Norte", "Sur", "Norte", "Este", "Oeste", "Este", "Sur", "Sur"]

conversion = CodificadorEtiqueta()
print("Original:", " - ", vector)
conversion.ajustar(vector)
print("Numérico:", " - ", conversion.transformar(vector))
print("Vuelta al original:", " - ", conversion.transformar_inv(conversion.transformar(vector)))

print("\nEscalar valores numéricos:\n")

vector0 = [5, 2, 6, 9, 3]
vector = np.array([[1, 7, 5, 2], [9, 6, 3, 4], [2, 1, 5, 6], [7, 8, 4, 6]])

escalar = Escalar()

print(vector0)
escalar.ajustar(vector0)
print(escalar.transformar(vector0))
print(escalar.transformar_inv(escalar.transformar(vector0)))
print("------------------------------------------------------------------------")
print(vector)
escalar.ajustar(vector)
print(escalar.transformar(vector))
print(escalar.transformar_inv(escalar.transformar(vector)))

print("\nConjunto de entrenamiento y test:\n")

x = np.random.randint(0, high=20, size=(5,2))
y = ['A'] * 3 + ['B'] * 2
resultado = divide_entrenamiento_test(x, tam_train=0.8)
print(resultado)
print("------------------------------------------------------------------------")
resultado = divide_entrenamiento_test(x, tam_train=2, semilla=123)
print(resultado)
print("------------------------------------------------------------------------")
resultado = divide_entrenamiento_test(x,y, tam_train=0.5, semilla=123)
print(resultado)
print("------------------------------------------------------------------------")
resultado = divide_entrenamiento_test(x, y, tam_train=0.9, semilla=123, balancear=y)
print(resultado)
