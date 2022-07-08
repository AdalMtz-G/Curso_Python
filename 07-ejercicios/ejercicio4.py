"""
Ejercicio 4.
Pedir dos números al usuario y hacer todas
las operaciones báscias de una calculadora y
mostrarlo por pantalla

"""
numero1 = int(input("Introduce el número 1: "))
numero2 = int(input("Introduce el número 2: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multiplicacion}\nDivisión: {division}")

print("###### VERSION CHIDA #######")

print("Suma: " + str(numero1 + numero2))
print("Resta: " + str(numero1 - numero2))
print("Multiplicación: " + str(numero1 * numero2))
print("División: " + str(numero1 / numero2))
