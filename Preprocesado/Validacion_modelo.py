import pandas as pd
import numpy as np


def divide_entrenamiento_test(*datos, tam_train, semilla=None, mezclar=True, balancear=None):
    lista = []
    if semilla is not None:
        np.random.seed(semilla);
    tamaño = len(datos[0])

    if mezclar is False and balancear is not None:
        raise ValueError("Mezclar tiene que ser True para usar balancear")

    if tam_train < 0:
        raise ValueError("tam_train tiene que ser un numero positivo")

    if tam_train > len(datos[0]):
        raise ValueError("tam_train tiene q ser menor a igual a la cantidad de datos")

    if mezclar and balancear is None:

        for estructura in datos:
            if len(estructura) != tamaño:
                raise Exception("All data structures must be the same size")
            if mezclar:
                estructura = barajar(estructura)
            if tam_train > 1:
                lista.append(estructura[:tam_train])
                lista.append(estructura[tam_train:])
            if 0 < tam_train < 1:
                i = int(len(estructura) * tam_train)
                lista.append(estructura[:i])
                lista.append(estructura[i:])

    else:

        clases = datos[1]
        valores = datos[0]

        if len(clases) != len(valores):
            raise ValueError("Values and Clases must be the same size!")

        disccionario = {}
        lista = [[], []]

        valores = np.array(valores)

        for i in range(len(clases)):
            if clases[i] in disccionario.keys():
                disccionario[clases[i]][0] += 1 / len(valores)
                disccionario[clases[i]].append(valores[i])
            if clases[i] not in disccionario.keys():
                disccionario[clases[i]] = [1 / len(valores)]
                disccionario[clases[i]].append(valores[i])

        if tam_train > 1:
            for clase in disccionario.keys():
                i = int((tam_train * disccionario[clase][0]))
                lista[0].extend(disccionario[clase][1:i + 1])
                lista[1].extend(disccionario[clase][i + 1:])

        if tam_train < 1:
            for clase in disccionario.keys():
                i = int((len(valores) * tam_train * disccionario[clase][0]))
                lista[0].extend(disccionario[clase][1:i + 1])
                lista[1].extend(disccionario[clase][i + 1:])

    return lista

def barajar(datos):
    if type(datos) is pd.DataFrame:
        datos_shuffled = datos.iloc[np.random.permutation(datos.index)].reset_index(drop=True)
    else:
        datos_shuffled = np.random.permutation(datos)
    return datos_shuffled

def original(lista, tipo_org):
    if tipo_org == 0:
        lista = pd.DataFrame(lista)
    elif tipo_org == 1:
        lista = np.array(lista)
    else:
        lista = lista
    return lista


