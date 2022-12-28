# List comprehensions

# Se trata de crear una lista: la primer parte es el elemento que va a hacer parte de la lista que será usada en el ciclo for

# [elemento iterado _ ciclo for que recorre el elemento]

# Creacion de lista en 3 lineas
numbers = []
for element in range(1,11):
    numbers.append(element*2)
print(numbers)

# Creacion de lista con list comprehension
numbers_v2 = [element for element in range(1,11)]
print(numbers_v2)

numbers_v2 = [element*2 for element in range(1,11)]
print(numbers_v2)

# Creación del ejercicio anterior con filtro
# [elemento iterado _ ciclo for que recorre el elemento _ condicion para filtrar elementos]
numbers_v3 = [element for element in range(1,11) if element%2==0]
print(numbers_v3)