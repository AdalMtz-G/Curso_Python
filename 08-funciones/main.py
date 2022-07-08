"""
FUNCIONES: 
Una funcions es un conjunto de instrucciones agreuadas bajo
un nombre concreto ue pueden reutilizarse invocando a 
la función tanas veces como sea necesario

def nombreDeMiFuncion(parametros):
    #BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
"""

"""

#Ejemplo 1
print("######### Ejemplo1 ##########")

def muestraNombres():
    print("Adal")
    print("Angel")

#Invocar función
muestraNombres()

#Ejemplo 2: Parametros
print("######### Ejemplo2 ##########")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre} y la edad es: {edad}")

mostrarTuNombre(nombre, edad)

"""

#Ejemplo 3
from typing import Text


print("######### Ejemplo3 ##########")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")

    for contador in range(1,11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

tabla(3)

#Ejemplo 4: paramtros opcionales
#None, False hacen los parametros opcionales

print("######### Ejemplo4 ##########")

def getEmpleado(nombre, ID = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if ID != None:
        print(f"ID: {ID}")

getEmpleado("Angel Adal")

#Ejemplo 5: paramtros opcionales
print("\n######### Ejemplo5 ##########")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Angel Adal"))

#Ejemplo 6
print("\n######### Ejemplo6 ##########")

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma) + "\n"
        cadena += "Resta: " + str(resta) + "\n"
    else:
        cadena += "Multiplicación: " + str(multi) + "\n"
        cadena += "División: " + str(division) + "\n"

    return cadena

print(calculadora(56,5,True))

#Ejemplo 7
print("\n######### Ejemplo7 ##########")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return  texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + " " + getApellidos(apellidos)
    return texto

print(devuelveTodo("Adal","Martinez"))

#Ejemplo 8 Funciones lambda: Una funcion que no tiene nombre, 
#no hace falta definirla con el def, su nombre, sus parametros ni tal,
#Son funciones anonimas, que sirven para tareas simples que pueden ser repetitivas
print("\n######### Ejemplo8 ##########")

dime_el_year = lambda year: f"El año es {year * 50}"

print(dime_el_year(2034))
