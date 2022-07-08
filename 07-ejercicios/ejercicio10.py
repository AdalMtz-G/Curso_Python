"""
Ejercicio 10.
El programa tiene que pedir la nota de 15 alumnos e imprimir cuantos alumnos
han aprobado y cuantos han reprobado.

"""
i = 1
r = 0
a = 0
for i in range (1, 16):
    calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
    if calificacion < 70:
        r += 1
    else:
        a += 1
    i += 1

print(f"Alumnos arpobados: {a}\nAlumnos reprobados: {r}")