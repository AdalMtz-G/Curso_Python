"""
#Condicional IF

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO: 
    Se ejecutan otro grupo de instrucciones

if condicion: 
    instrucciones
else:
    otras instrucciones

#Operadores de comparación
== igual
!= diferente 
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

#Operadores lógicos
and Y
or O
! negacion
not no

"""
# Ejemplo 1
print("########## EJEMPLO 1 #############")

color = "rojo"
#color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("Cocojiko")
    print("El color es ROJO")
else: 
    print("Color incorrecto")

# Ejemplor 2

print("\n########## EJEMPLO 2 #############")

year = 2020 
#year = int(input("¿En qué año estamos?: "))

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")

# Ejemplor 3

print("\n########## EJEMPLO 3 #############")

nombre = "Angel Martínez"
ciudad = "Nuevo León"
continente = "Oceania"
edad = 20
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "America":
        print("El ususario no es Americano")
    else:
        print(f"Es Americano y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplor 4

print("\n########## EJEMPLO 4 #############")
dia = 2
#dia = int(input("Introduce el número de la semana: "))

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")
"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

# Ejemplor 5

print("\n########## EJEMPLO 5 #############")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))
edad_oficial = 16

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No está en edad de trabajar")

# Ejemplor 6

print("\n########## EJEMPLO 6 #############")

pais = "Mexico"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")


# Ejemplor 7

print("\n########## EJEMPLO 7 #############")


pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} SÍ es un país de habla hispana")


# Ejemplor 8

print("\n########## EJEMPLO 8 #############")


pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} SÍ es un país de habla hispana")
