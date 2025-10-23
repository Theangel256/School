A = [[0,1,3], [5,2,9]]
B = [[1,3,2], [2,3,1]]
def suma_de_las_matrices(A, B, m, n):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):  
            C[i].append(A[i][j] + B[i][j])
    return C
#LA FUNCION RECORRE LAS PRIMERAS DOS LISTAS DE TIPO INT DESDEEL DATO 0 AL 2 PARA
print(suma_de_las_matrices(A, B, 3, 3))