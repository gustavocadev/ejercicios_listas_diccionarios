"""
Ejercicio 1
Crea un programa que recorra una lista y cree un diccionario que contenga el número de veces que
aparece cada número en la lista.
• Ejemplo: [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
• Resultado: {12: 3, 23: 2, 5: 3, 92: 2, 29: 1, 64: 1}

"""

nums = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]

numeros_veces = {}
for num in nums:
    numeros_veces.update({num: nums.count(num)})

print(numeros_veces)
