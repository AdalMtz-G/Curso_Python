"""
Ejercicio 3.
Escribir un programa que muestre los cuadrados
de los 60 primeros números naturales.
Resolverlo con for y con while

"""

i = 1

print("FOR")
for i in range (1, 61):
    print(f"Número {i}, Cuadrado del número: {pow(i, 2)}")

i = 1

print("\nWHILE")
while i <= 60:
    print(f"Número {i}, Cuadrado del número: {pow(i, 2)}")
    i += 1

