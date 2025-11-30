def fact(n):
    result= n
    i = 1
    while i < n:
        result = result*(n-i)
        i = i+1
    print(result)

fact(9)