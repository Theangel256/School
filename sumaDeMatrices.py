def suma(matriz1: list[list[int]], matriz2: list[list[int]], matriz3: list[list[int]]) -> list[list[int]]:
     """
    Suma dos matrices de 3x3 y almacena el resultado en una tercera matriz.

    Args:
        matriz1 (List[List[int]]): Primera matriz de enteros de tamaño 3x3.
        martiz2 (List[List[int]]): Segunda matriz de enteros de tamaño 3x3.
        martiz3 (List[List[int]]): Matriz donde se almacenará el resultado de la suma.

    Returns:
        List[List[int]]: La matriz resultante (matriz3) con la suma de matriz1 y matriz2.

    Nota:
        La operación modifica matriz3 directamente.
    """
     for i in range(3):
        for j in range(3):
            matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
     return matriz3
a = ([1, 2, 3],
     [ 4, 5, 6],
     [7, 8, 9 ])

b = ([10, 11, 12],
     [ 13, 14, 15],
     [ 16, 17, 18 ])

c = ([0, 0, 0],
     [ 0, 0, 0],
     [0, 0, 0 ])

print(suma(a,b,c))