"""
Ejercicio 2
Recorre un diccionario y crea una lista solo con los valores que contiene, sin añadir valores
duplicados.
    • Ejemplo: {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,
    'Maite': 5}
    • Resultado: [3, 8, 12, 5, 7]
"""


names = {
    'Mikel': 3,
    'Ane': 8,
    'Amaia': 12,
    'Unai': 5,
    'Jon': 8,
    'Ainhoa': 7,
    'Maite': 5
}
nums = list(names.values())

# instancia
nuevo_set = set()
uniqueNums = []

for num in nums:
    if num not in nuevo_set:
        uniqueNums.append(num)
        nuevo_set.add(num)

print(uniqueNums)
