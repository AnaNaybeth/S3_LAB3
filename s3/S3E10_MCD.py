ab1=int(input("ingresa un numero:"))
ab2=int(input("ingresa un numero:"))
def mcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(mcd(ab1,ab2))