
print("Dame una lista a sumar")
num = list(input("Lista de numeros: "))
def suma(l, i):
    if i==len(l)-1:
        return l[i]
    else:
        return l[i]+suma(l, i+1)
print(suma(num, 0))