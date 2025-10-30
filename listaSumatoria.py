def suma(l):
    i = 0
    n = len(l)
    suma = 0
    while i < n:
        suma = suma+l[i]
        i = i+1
    print(l)
    print(n)

suma([1,3,2,4,-1,5,2])