Lista=input("Ingresa una lista de numeros separada por espacios:")
def mediana():
    l=[int(x) for x in Lista.split()]
    ac=l.sort()
    lon=len(l)
    if lon%2!=0:
        return l[lon//2]
    else:
        return(l[lon//2-1]+l[lon//2])/2

print(mediana())