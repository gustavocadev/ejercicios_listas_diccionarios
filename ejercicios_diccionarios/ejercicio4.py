"""
Ejercicio 4
Crea un programa que permita introducir a un profesor las notas de sus estudiantes (máximo 10
estudiantes). Los datos se deberán almacenar en un diccionario como el siguiente:
estudiantes = {
    "1": {
        "nombre": "Lorea",
        "nota": 8
    },
    "2": {
        "nombre": "Markel",
        "nota": "4.2"
    },
    "3": {
        "nombre": "Julen",
        "nota": 6.5
    }
}
Una vez introducidos todos los datos, el programa mostrará una lista con los nombres de los
estudiantes que han suspendido y otra con los que han aprobado. También calculará y mostrará
la nota media de la clase.
"""


def calcular_media(total_datos, suma_de_datos):
    media = suma_de_datos / total_datos
    return media


# diccionario vacio
estudiantes = {}

# número de estudiantes
numero_estudiantes = 10
# Bucle para pedir datos y agregar datos
while numero_estudiantes > 0:

    nombre_estudiante = input('ingrese el nombre del estudiante: ')
    nota_estudiante = float(input('ingrese la nota del estudiante: '))
    print('---------------')
    estudiantes.update({str(len(estudiantes) + 1): {
        "nombre": nombre_estudiante,
        'nota': nota_estudiante
    }})
    numero_estudiantes -= 1

# lista vacia
nombres_estudiantes = []
for key in estudiantes:
    # Guardo el nombre del estudiante en la lista vacia
    nombres_estudiantes.append(estudiantes[key]['nombre'])
print(
    f'la lista con los nombres de los estudiantes es: { nombres_estudiantes }')

# variable acumuladora de notas
suma_de_notas = 0
for key in estudiantes:
    notas_estudiantes = estudiantes[key]['nota']
    suma_de_notas += notas_estudiantes

media_notas = calcular_media(len(estudiantes), suma_de_notas)

print(f'la nota media de la clase es: { round(media_notas, 2) }')
