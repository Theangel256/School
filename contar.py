# Función para contar cuántas veces aparece un número en una lista 
# usando un bucle while
def contar(lista, numero_buscado):
    # Parámetros:
    # lista (list): La lista en la que se buscará el número.
    # numero_buscado: El número que se desea contar en la lista.
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
print(f"El número {numero} aparece {resultado} veces en la lista")