def busqueda_binaria_primera_ocurrencia(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    resultado = -1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            resultado = medio
            derecha = medio - 1  # seguir buscando a la izquierda (primera aparición)
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return resultado


# Ejemplo de prueba (puedes dejarlo o quitarlo)
if __name__ == "__main__":
    datos = [1, 2, 2, 2, 5, 7, 9]
    print(busqueda_binaria_primera_ocurrencia(datos, 2))  # debe imprimir 1
