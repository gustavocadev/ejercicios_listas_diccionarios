"""
Dada la siguiente lista [12, 23, 5, 29, 92, 64] realiza las siguientes operaciones y vete mostrando
la lista resultante por pantalla:
    1. Elimina el último número y añádelo al principio.
    2. Mueve el segundo elemento a la última posición.
    3. Añade el número 14 al comienzo de la lista.
    4. Suma todos los números de la lista y añade el resultado al final de la lista.
    5. Fusiona la lista actual con la siguiente: [4, 11, 32]
    6. Elimina todos los números impares de la lista.
    7. Ordena los números de la lista de forma ascendente.
    8. Vacía la lista.

    Resultado:
    [64, 12, 23, 5, 29, 92]
    [64, 23, 5, 29, 92, 12]
    [14, 64, 23, 5, 29, 92, 12]
    [14, 64, 23, 5, 29, 92, 12, 239]
    [14, 64, 23, 5, 29, 92, 12, 239, 4, 11, 32]
    [14, 64, 92, 12, 4, 32]
    [4, 12, 14, 32, 64, 92]
    []

"""
nums = [12, 23, 5, 29, 92, 64]

# Elimina el último número y añádelo al principio.
nums.pop()
nums.insert(0, 64)
print(nums)
# Mueve el segundo elemento a la última posición.
nums.remove(12)
nums.append(12)
print(nums)
# Añade el número 14 al comienzo de la lista.
nums.insert(0, 14)
print(nums)
# Suma todos los números de la lista y añade el resultado al final de la lista.
suma = 0
for num in nums:
    suma += num
nums.append(suma)
print(nums)

# Fusiona la lista actual con la siguiente: [4, 11, 32]
nums.extend([4, 11, 32])
print(nums)

# Elimina todos los números impares de la lista.


def deleteParsNumbers(numbers):
    numeros_pares = []
    for num in numbers:
        if num % 2 == 0:
            numeros_pares.append(num)
    return numeros_pares


# Elimina todos los números impares de la lista.
nums = deleteParsNumbers(nums)
print(nums)

# Ordena los números de la lista de forma ascendente.
nums.sort()
print(nums)

# Vacía la lista.
nums.clear()
print(nums)
