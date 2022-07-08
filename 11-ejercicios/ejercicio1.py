"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- En una funcion que devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

menu = """
///////////////MENU/////////////////////
1.- Mostrar lista
2.- Ordenar lista
3.- Mostrar longitud de la lista
4.- Buscar un elemento de la lista
5.- Recorrer lista y devolver un string
6.- Salir
"""
lista = [2, 3, 6, 1, 5, 8, 4, 7]
pop = True

def mostrarLista():
    for numero in lista:
        print(numero)

def ordenarLista():
    lista.sort()
    return print(f"Lista ordenada: {lista}")

def longitudLista():
    return print(f"Longitud de la lista: {len(lista)}")

def buscarEnLaLista(lista):
    numero = int(input("Numero deseado: "))
    if numero in lista:
        print("El numero esta en la lista")
    else:
        print("El numero no existe en la lista")

def cadenaLista(lista):
    resultado = ""
    for numero in lista:
        resultado += "Elemento" + str(numero)
        resultado += "\n"
    return resultado



while pop == True:
    print(menu)
    r = int(input("Respuesta: "))
    if r == 1:
        mostrarLista()
    elif r == 2:
        ordenarLista()
    elif r == 3:
        longitudLista()
    elif r == 4: 
        buscarEnLaLista(lista)
    elif r == 5:
        print(cadenaLista(lista))
    elif r == 6:
        pop = False
    else:
        print("Opcion invalida")
