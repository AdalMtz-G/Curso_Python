from traceback import print_tb


cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1, 2, 5, 8, 3, 4]

#Ordenar
print(numeros)
numeros.sort()  # .sort Funciona para ordenar una lista
print(numeros)
cantantes.sort()
print(cantantes)

# Anadir elementos
cantantes.append("Natos y Waor")    # Funciona para agregar elementos a la lista

cantantes.insert(1, "David Bisbal") # Funciona con dos parametros .insert(posicion, elemento)
# para agregar elementos en cierta posicion
print(cantantes)

# Eliminar elementos
cantantes.pop(1) # Elimina el indice que se indica, posicion [0, 1, ...]
print(cantantes)
cantantes.remove('Bad Bunny')   # Elimina el elemento exacto pedido
print(cantantes)

# Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes) # Busca un elemento dentro de una lista y retorna True or False

# Contar elementos
print(cantantes)
print(len(cantantes))

# Cuantas veces aparece un elemento
print(numeros)
numeros.append(8)
print(numeros)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Drake"))

# Unir listas
cantantes.extend(numeros)   # A cantantes le agrego numeros
print(cantantes)