"""
Matrices en Algebra Lineal:

A =  0  -1  3
  [  5   2  -9  ]
     6 -0.1 10
"""
matriz_A = [[0,-1,3],[5,2,-9],[6,-0.1,10]]

for filas in matriz_A:
    for columnas in filas:
        print(columnas)

for i in range(3):
    for j in range(3):
        print(matriz_A[i][j])