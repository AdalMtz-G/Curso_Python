"""
Ejercicio 8.
¿Cuánto es el c por ciento de x número?

"""
numero = float(input("Ingrese el número a sacar el porcentaje: "))
porcentaje = float(input("Ingrese el porcentaje que quiera sacar: "))

# operacion = (numero * (porcentaje/100))

print(f"El {porcentaje}% de {numero} es {(porcentaje * numero)/100}")