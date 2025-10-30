
print("Dame un numero factorial")
num = int(input("ES el factor: "))
def fact(n):
    if n==0:
        return 1
    else:
        print(n)
        return n*fact(n-1)
print(fact(num))