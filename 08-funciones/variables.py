"""
Variables locales: Se definen dentro de la función y no se puede
usar fuera de ella, solo están disponibles dentro. A no ser que hagamos
uso de un return

Variables globales: Son las que se declaran fuera de una función y estan disponibles
dentro y fuera de ellas

"""

#Variable global
frase = "Ni los genios son tan genios, ni los mediocres son tan mediocres"

print(frase)

def holaMundo():
    #Variable local
    frase = "Hola mundo"
    print(frase)

    global website
    website = "adal.es"


holaMundo()
print(website)