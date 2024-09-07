Lista=input("Ingresa una lista de numeros separada por espacios:")
def smay():
    l=[int(x) for x in Lista.split()]
    l.sort(reverse=True)
    return l[1]
print(smay())