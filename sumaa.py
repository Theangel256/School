print("Dame un numero a sumar")
num = int(input("Numero a sumar: "))
def suma(n):
    if n==1:
        return 1
    else:
        print(n)
        return n+suma(n-1)
print(suma(num))