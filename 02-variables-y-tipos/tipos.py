nada = None
cadena = "Hola soy Angel Martínez"
entero = 99
flotante = 4.2
booleano = True
lista = [10, 20, 30, 100, 200]
listaString = [44, "treinta", 30, "cuarenta"]
tuplaNoCambia = ("Master", "en", "python")           #Lista de datos que no pueden cambiar
diccionario = {
    "nombre": "Angel",
    "apellido": "Martínez",
    "curso": "Master en python"
}
rango = range(9)
dato_byte = b"Probando"

#Imprimir variables
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCambia)
print(diccionario)
print(rango)
print(dato_byte)


#Mostrar tipo de dato
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(listaString))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))



print("-----------------------------------------------------------------------")
print("Convertir tipos de dato")


texto = "Hola soy un texto"
numero = str(776)
print(type(numero))

# 776
# "776"

print(texto + " " + numero)


numero = int(776)
print(type(numero))

numero = float(776)
print(type(numero))
