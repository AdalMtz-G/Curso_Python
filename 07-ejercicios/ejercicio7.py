"""
Ejercicio 7.
Hacer un programa que muestre todos los números impares
entre dos números que deida el usuario.

"""

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese un número(2): "))

if numero2 < numero1:
    comodin = numero2
    numero2 = numero1
    numero1 = comodin

i = numero1
print(f"Los números entre {numero1} y {numero2} son:\n")
for i in range (numero1 + 1, numero2):
    if i % 2 != 0:
        print(i)
    i += 1
