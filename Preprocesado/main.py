from Preprocesado.Escalar import Escalar

prueba = [[5,9,1,3], [2,8,4,6], [4,5,-1,9], [4,5,-1,9]]
list = [[0.0, 1.0, -1.0, -0.5], [-1.0, 1.0, -0.3333333333333333, 0.3333333333333333], [0.0, 0.2, -1.0, 1.0], [0.0, 0.2, -1.0, 1.0]]

escalar = Escalar()

escalar.ajustar(prueba)
print(escalar.transformar(prueba))
print(escalar.transformar_inv(list))


