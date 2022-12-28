# Ejercicio: creación de diccionario con list comprehensions a partir de una lista
import random
countries = ['col', 'mex', 'bol', 'pe']
population_v2 = {country:random.randint(1,100) for country in countries}
print(population_v2)

# Se hará filtro cn comprehensions al diccionario segun population del pais
result = {country: population for (country, population) in population_v2.items() if population > 50}
print(result)

# Ejercicio 2: Crear diccionario solo con las vocales de una frase

texto = 'Hola, soy Daniel'
unique = { c: c.upper() for c in texto if c in 'aeiou'}
print(unique) # tener en cuenta que como se trata de diccionario no se repite la clave, por lo que las vocales repetidas se van actualizando en el diccionario

# Solución a la situación del ejercicio anterior en el sentido de que se indique la frecuencia de clave en vez de la vocal
unique_v2 = {i:texto[i].upper() for i in range(len(texto)) if texto[i] in 'aeiou'}
print(unique_v2)

# Play ground list comprehension


# Ejercicio

""" 
Para resolver este desafío, tu reto es refactorizar el código base utilizando la característica de "List Comprehension" de Python.

El código base incluye una lista llamada numbers que contiene números pares e impares. El algoritmo actual selecciona los números pares de esta lista y los agrega a una nueva lista llamada even_numbers.

Tu reto es crear la misma lista utilizando la característica de "List Comprehension" de Python para crear la lista de números pares de manera más concisa y eficiente y el resultado debería quedar en la variable even_numbers_v2. Las dos técnicas deberían de dar el mismo resultado.

Ejemplo:

Input:
[35, 16, 10, 34, 37, 25]

Output:
v1 => [16, 10, 34]
v2 => [16, 10, 34]
"""

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 => ', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = []
# Version Daniel
#even_numbers_v2 = [even_numbers_v2.append(number) or number for number in numbers if number % 2 == 0 ]
# Versión Platzi
even_numbers_v2 = [number for number in numbers if number % 2 == 0]
print('v2 => ', even_numbers_v2)