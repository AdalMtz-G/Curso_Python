"""
Ejercicio 9.
Hacer un programa que pida números al usuario
indefinidamente hasta meter el número 111

"""
numero = int(input("Ingrese un número: "))
while numero != 111:
    print(f"Número: {numero}")
    numero = int(input("Ingrese un número: "))
    
