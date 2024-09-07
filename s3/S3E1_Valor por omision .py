def nomed(nombre,edad=18):
    if edad<0:
        print("Su edad no puede estar en numeros negativos")
    else:
        print("Su nombre es",nombre,"y tiene",edad,"años")
nomed("Raul")
nomed("Sofia",20)