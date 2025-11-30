n = 7
numEspInt = n-2
numEspExt = 0
for i in range((n+1)//2):
    # espacios externos
    for j in range(numEspExt):
        print(" ", end="")
    #primer asterisco
    print("*", end="")
    if i == 0:
        for nose in range(n-1):
            print("*", end="")
    if numEspInt > 0 & i != 0:
        for j in range(numEspInt):
            print(" ", end="")
        print("*", end="")

    print() # Nueva linea

    # actualizar espacios
    numEspExt += 1
    numEspInt -= 2

# mitad inferior
numEspInt -= 1
iInicialMitadInferior = n-(n//2)
numEspExt += n-iInicialMitadInferior-1
#Ciclo para iterar los renglones
for i in range(iInicialMitadInferior, n):
    # Imprimir espacios externos
    for j in range(numEspExt):
        print(" ", end="")
    # Imprimir el 1er asterisco
    print("*", end="")
    if i == n-1:
        for nose in range(n-2):
            print("*", end="")
    # Imprimir los espacios internos
    if i != n-1:
        for j in range(numEspInt):
            print(" ", end="")
    # Imprimir el último asterisco
    print("*")

    # actualizar espacios
    numEspExt -= 1
    numEspInt += 2
