# Map: Es una función que hace transformaciones a una lista dada de elementos. Funciona como una High Order Function, es decir se puede enviar un lambda como parametro. Se obtiene luego de la transformación la misma cantidad de elementos de la lista pero modificados. La función map() crea una nueva lista y en ocasiones modifica la lista original y la resultante

# Ejercicio que modifica los datos de una lista y los guarda en otra lista
numbers = [1,2,3,4]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

# Ejercicio anterior usando map()
numbers_v3 = map(lambda i: i * 2, numbers)
print(numbers_v3) # Devuelve el objeto, para conocer los datos debe convertirse en lista
print(list(numbers_v3))

# Otra aplicacion practica para iterar con listas y map()
number_1 = [1,2,3,4]
numers_2 = [5,6,7]
result = list(map(lambda x,y : x+y, number_1,numers_2))
print(number_1)
print(numers_2)
print(result) # opera las listas con el tamaño de la lista más pequeña