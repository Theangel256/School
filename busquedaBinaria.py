def busquedaBinaria(lista: list[int], e: int) -> bool: 
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        medio = (inicio+final)//2
        if lista[medio] == e:
            return True
        elif lista[medio] < e:
            inicio = medio + 1
        else:
            final = medio - 1
    return False
print("    Lista ordenada de ejemplo: [1,2,3,4,5,6,7,8,9,10]")
valorABuscar = int(input("    Ingrese el valor a buscar: "))
print("    Busqueda Binaria usando while")
print(busquedaBinaria([1,2,3,4,5,6,7,8,9,10], valorABuscar))