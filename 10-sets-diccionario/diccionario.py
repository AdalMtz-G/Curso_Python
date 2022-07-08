"""
Diccionario:
Un tipo de dato que almacena un cojunto de datos.
En formato clave > valor
Es parecido a un array asociativo o un objeto json.
"""

from pandas import concat


persona = {
    "nombre": "Victor",
    "apellidos": "Robles",
    "web": "victorroblesweb.es"
}

print(persona)
print(type(persona))
print(persona["web"])


# Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]

contactos[0]['nombre'] = "Antonito"
print(contactos[0]['nombre']) # [Indice del diccionario] [Indice del texto]


# Listado completo de contcacto
print("\nListado de contactos: ")
print("------------------------------------------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("------------------------------------------------------------------")