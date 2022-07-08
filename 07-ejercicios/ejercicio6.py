"""

Ejercicio 6.
Mostrar todas las tablas de multiplicar del 1 al 10
Mostrando el titulo de la tabla y luego las multiplicaciones

"""

i = 1
j = 1

for i in range (1, 11):
    print(f"Tabla del {i}")
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1
    j = 1
    print("\n")