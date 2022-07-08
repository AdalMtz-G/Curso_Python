"""
Ejercicio 2.
Escribir un script que nos muestre por pantalla
todos los números pares del 1 al 120

"""
i = 1

while i <= 120:
    if i % 2 == 0:
        print(f"Número: {i}")
    i += 1


print("\nEl programa ha terminado")