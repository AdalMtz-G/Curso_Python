nombre = "Angel Martinez"

#Funciones generales
print(nombre)
print(type(nombre))

#Detectar el tipado
#Comprueba que tipo de variable es
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un número con decimales")

#Limpiar espacios

frase = "         mi contenido          "
print(frase)
print(frase.strip())


#Eliminar variables

year = 2021
print(year)

del year
#print(year)

#Comprobar variable vacia
texto = "  faff "

if len(texto) <= 0: 
    print("La variable esta vacia")
else: 
    print("La variable tiene contenido: ",len(texto))


#Encontrar caracteres
#Envia la posicion en la quee empieza la string
frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)


#Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())

