"""
Ejercicio 2
Crea un programa que solicite al usuario 5 números y los guarde en una lista. A continuación el
programa pedirá otros 5 números al usuario almacenándolos en una segunda lista. El programa
mostrará al usuario una lista que contenga los números que tienen en común las dos listas anteriores.
    • Ejemplo: Lista 1 = [6,14,11,78,5] y Lista 2 = [3,14,22,78,9]
    • Resultado: [14, 78]
"""

numbers1 = []
numbers2 = []


def numerosRepetidos():
    numeros_comunes = []

    for i in range(len(numbers1)):

        if numbers1[i] == numbers2[i]:
            numeros_comunes.append(numbers1[i])

    return numeros_comunes


for i in range(5):
    num = int(input("ingrese un número: "))
    numbers1.append(num)

print('-------------')
for i in range(5):
    num = int(input("ingrese un número: "))
    numbers2.append(num)

numeros_comunes = numerosRepetidos()

print('-------------')
print(f"los números comunes son: {numeros_comunes}")
