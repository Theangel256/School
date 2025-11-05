# Función para contar cuántas veces aparece un número en una lista 
# usando un bucle while
def contar(lista: list[int], numero_buscado: int) -> int:
    # Parámetros:
    # lista (list): La lista en la que se buscará el número.
    # numero_buscado (int): El número que se desea contar en la lista.
    # Retorna:
    # int: El número de veces que el número aparece en la lista.
    contador = 0
    i = 0
    # Bucle while para recorrer la lista
    while i < len(lista):
        # Comparar el elemento actual con el número buscado
        # Si son iguales, incrementar el contador
        if lista[i] == numero_buscado:
            contador += 1
        # Incrementar el índice para pasar al siguiente elemento
        i += 1
    # Retornar el contador final
    return contador

# Ejemplo de uso
numeros = [1, 2, 3, 2, 4, 2, 5]
numero = 2
# Llamar a la función contar y mostrar el resultado
resultado = contar(numeros, numero)
print("    Contar usando while, Iterando sobre la lista")
print(f"    El número {numero} aparece {resultado} veces en la lista")

def contarRecursivo(l: list[int], e: int) -> int:
    """
    Cuenta cuántas veces aparece un elemento en una lista de forma recursiva.

    Parámetros:
    l (list): La lista en la que se buscará el elemento.
    e (int): El elemento que se desea contar en la lista.

    Retorna:
    int: El número de veces que el elemento aparece en la lista.
    """
    # Caso base: si la lista está vacía, retornar 0
    if not l:
        return 0
    else:
        # Verificar si el primer elemento es igual al elemento buscado
        if l[0] == e:
            # Si es igual, sumar 1 y llamar recursivamente con el resto de la lista
            return 1 + contarRecursivo(l[1:], e)
        else:
            # Si no es igual, llamar recursivamente con el resto de la lista sin sumar
            return contarRecursivo(l[1:], e)
        
# Ejemplo de uso
numeros = [1, 5, 3, 2, 4, 2, 5, 6, 1, 5, 5, 7, 5, 8, 5, 9, 1]
numero = 5
# Llamar a la función contar y mostrar el resultado
resultado = contarRecursivo(numeros, numero)
print("    Contar usando while, Recursivamente sobre multiples listas chicas")
print(f"    El número {numero} aparece {resultado} veces en la lista")