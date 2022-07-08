"""

Una variable es un contenedor de información
que dentro guradar un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto

"""

#Mostrar valores de las variables
texto = "Master en Python"
texto2 = "con Angel Martínez"
numero = 45
decimal = 6.7

print(texto)
print(texto2)
print(numero)
print(decimal)

print("---------------------------------")

numero = 77
decimal = 8.9

print(numero)
print(decimal)


#Concatenación
nombre = "Angel"
apellidos = "Martínez"
web = "adalmtzweb0s.es"
x = f"{nombre} {apellidos}"

print(f"x es: {x}")

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es {}".format(nombre,apellidos,web))