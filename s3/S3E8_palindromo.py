cade=input("Ingrese una cadena de texto: ")
def palin(cad):
    inv=cade[::-1]
    if inv==cade:
        return ("palindromo")
    else:
        return ("No es palindromo")
print(palin(cade))
