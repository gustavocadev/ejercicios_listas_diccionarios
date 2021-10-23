"""
Ejercicio 3
Crea una programa de Login que compruebe el usuario y contraseña en el diccionario a continuación:
usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}
El usuario tendrá un máximo de 3 intentos, y al acceder correctamente se mostrará el nombre y
apellido del usuario.
"""

usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}


usuarios = usuarios.values()

intentos = 3

while intentos > 0:
    nombre = input('ingrese su nombre: ')
    apellido = input('ingrese su apellido: ')
    password = input('ingrese su password: ')

    print('---------------')

    encontrado = False
    for usuario in usuarios:
        if nombre.lower() == usuario['nombre'].lower() and apellido.lower() == usuario['apellido'].lower() and password == usuario['password']:
            print(f'Tu nombre es: { nombre.capitalize() }')
            print(f'Tu apellido es: { apellido.capitalize() }')
            encontrado = True
            break

    if encontrado == True:
        break
    intentos -= 1
