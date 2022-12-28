# Dictionary comprehensions
# [key:value for var in iterable]

# Ejercicio sin comprenhension
dict = {}
for i in range(1,11):
    dict[i]= i*2
print(dict)

# Ejercicio con comprehensions
dict_v2 = {i:i*2 for i in range(1,11)}
print(dict_v2)

# Ejercicio: creación de diccionario con list comprehensions a partir de una lista
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
print(population)

# Ejercicio anterior con comprehensions
population_v2 = {country:random.randint(1,100) for country in countries}
print(population_v2)

# Ejercicio: creación de diccionario desde dos listas
names = ['nico', 'zule', 'santi']
ages = [12,56,98]
# Resultado esperado
{
    'nico': 12,
    'zule': 56,
    'santi': 98
}

# Solución sin comprehension
print(zip(names, ages)) # Solo imprime el objeto; la funcion zip une las listas
print(list(zip(names,ages))) # Para imprimir se convierte en lista y arroja la lista con tuplas internas. Tener en cuenta que las listas deben tener el mismo tamaño para que maneje todos los valores

# Solución con comprehensions
new_dict = {names: ages for (names, ages) in zip(names, ages)}
print(new_dict) # Imprime el diccionario

# Diccionario con filtro en comprehension
new_dict_v2 = {names:ages for (names, ages) in zip(names, ages) if ages >= 18}
print(new_dict_v2)