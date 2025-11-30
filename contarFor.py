def contar(l,e):
    """
    Cuenta cuántas veces aparece un elemento en una lista.

    Parámetros:
    l (list): La lista en la que se buscará el elemento.
    e: El elemento que se desea contar en la lista.

    Retorna:
    int: El número de veces que el elemento aparece en la lista.
    """
    contador = 0
    for elemento in l:
        if elemento == e:
            contador += 1
    return contador
# Ejemplo de uso
if __name__ == "__main__":
    lista = [1, 2, 3, 1, 4, 1, 5]
    elemento_a_contar = 1
    resultado = contar(lista, elemento_a_contar)
    print(f"El elemento {elemento_a_contar} aparece {resultado} veces en la lista.")