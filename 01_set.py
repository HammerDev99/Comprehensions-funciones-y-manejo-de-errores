## Conjuntos

# Son estructuras donde sus variables contenidas no tienen un orden especifico

set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_dif_types = {1, False, 'Hola'} # Los ordena y no importa el tipo de dato
print(set_dif_types)

set_from_string = set('hoola') # Conjunto a partir de un string. No admite valores repetidos y se aplica la funcion set a la cadena
print(set_from_string)

set_from_tuples = set(('abc', 'def', 'hij', 'abc')) # Asimismo como con una cadena no admite valores repetidos de una tupla
print(set_from_tuples)

numbers = [1,2,3,4,1,2,3]
set_from_list = set(numbers) # Asimismo como con una cadena no admite valores repetidos de una lista
print(set_from_list)
unique_numbers = list(set_from_list) # Ejercicio para determinar los numeros unicos pasandolos a un set y de nuevo a una lista
print(unique_numbers)


