from Preprocesado.Escalar import Escalar

prueba = [[6.6, 4.5, 7], [7 ,9, 4]]
lista = [[0.6799999999999997, -1.0, 1.0], [0.2, 1.0, -1.0]]

escalar = Escalar()

escalar.ajustar(prueba)
print(escalar.transformar(prueba))
print(escalar.transformar_inv(escalar.transformar(prueba)))


