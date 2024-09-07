num=int(input("ingresa un numero:"))
def factorial(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r
print(factorial(num))
