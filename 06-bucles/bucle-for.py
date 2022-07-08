"""
# FOR

for variable in elemento iterables (lista, rango, etc)
    BOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contador in range (0, 5):
    print("Voy por el número "+ str(contador))
    
    resultado += contador

print(f"El resutado es: {resultado}")

# Ejemplo tablas de multiplicar
print("\n########### EJEMPLO ###########")

numero_usuario = int(input("¿De qué número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n### Tabala de multiplicar del número {numero_usuario} ####")

for numero_tabla in range(1, 11):
        
    if numero_usuario == 45:
        print("No se pueden mostrar números prohibidos !!")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")

else:
    print("Tabla finalizada.")