lista=input("Ingrese una lista de numeros separados por espacio:")
def prom(cal):
    cal=[int(x) for x in lista.split()]
    s=sum(cal)
    n=len(cal)
    prom=s/n
    return prom
print(prom(lista))