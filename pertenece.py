def pertenece(l: list[int], elemento: int) -> bool:
    """Devuelve True si `elemento` pertenece a la lista `l` usando while."""
    i = 0
    while i < len(l):
        if l[i] == elemento:
            return True
        i += 1
    return False
print("    Lista ordenada de ejemplo: [1,2,3,4,5,6,7,8]")
valorABuscar = input("    Ingrese el valor a buscar: ")
print("    Busqueda iterativa usando while")
print(pertenece([1,2,3,4,5,6,7,8], int(valorABuscar)))