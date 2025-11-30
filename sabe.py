# 1.- Elevar un numero a la potencia de n (n > 0)
def elevar (a,n):
    if n == 0:
        return 1
    else: 
        return a *elevar(a, n-1)
print(elevar(a = 5, n = 3))
# 2.- Invertir la palabra concatenada
print()
def invertir (s, i ):
    if i==0:
        return s[i]
    else:
        return s[i]+invertir(s, i-1)
print(invertir("Hola", i = 3))
    
    

