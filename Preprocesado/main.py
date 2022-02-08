from Preprocesado.Escalar import Escalar

prueba = [100, 120, 160, 76]
prueba_inv = [-0.4285714285714284, 0.047619047619047894, 1.0, -0.9999999999999998]

escalar = Escalar()

escalar.ajustar(prueba)
print(escalar.transformar(prueba))
print(escalar.transformar_inv(prueba_inv))


