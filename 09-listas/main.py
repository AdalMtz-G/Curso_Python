"""
LISTAS (ARRAYS)

Son  colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores  podemos usar un índice númerico.
"""
"""

pelicula = "Batman"

# Definir Lista
peliculas = ["Batman","Spiderman","El señor de los anillos"]
cantantes = list(('2pac','Drake','Jennufer Lopes'))
years = list(range(2020,2050))
variadas  = ["Victor",30,4.4,True,"Texto"]


print(peliculas)
print(cantantes)
print(years)
print(variadas)

# Índices
print(peliculas[1])
print(peliculas[-2]) #Muestra el número 2, contando de atras hacia adelante
print(cantantes[1:3])
print(cantantes[0:3]) #Muestra del 0 al 3
print(peliculas[1:]) #Muestra del 1 en adelante

#Añadir elemento a Lista
cantantes.append("Kase O")
cantantes.append("Natos y waor")
print(cantantes)

#Recorrer Lista

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n############LISTADO DE PELICULA##################")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1} {pelicula}")


"""

# Listas multidimensionales

print("\n############LISTADO DE CONTACTOS##################")

contactos = [  ['Antonio','antonio@antonio.com'],['Luis','luis@luis.com'],['Salvador','salvador@salvador.com'] ]

"""
print("\nContactos\n")
for contacto in contactos:
    print(contacto[0])
"""


for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

#print(contactos[1][1])