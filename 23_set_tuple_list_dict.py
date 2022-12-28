# Set
set_countries = {'col', 'mex', 'bol'}
print('Tipo de objeto: ',type(set_countries))
print('Objeto completo: ',set_countries)
print('Objeto iterado:')
for i in set_countries:
    print(type(i))
    print(i)
""" 
Operaciones:
set_countries.add('NuevoDato')
 """

print('\n','***'*5)

# Tupla
tupla = (2,3,4,5)
print('Tipo de objeto: ',type(tupla),type(tupla[0]))
print('Objeto completo: ',tupla)
print('Objeto iterado:')
for i in tupla:
    print(i)

print('\n','***'*5)

# Lista simple
lista_simple = [1,3,'Hola',4.6]
print('Tipo de objeto: ',type(lista_simple), type(lista_simple[2]))
print('Objeto completo: ',lista_simple)
print('Objeto iterado:')
for i in lista_simple:
    print(i)
"""
# Operaciones más comúnes
lista[i]: Devuelve el elemento que está en la posición i de la lista.
lista.pop(i): Devuelve el elemento en la posición i de una lista y luego lo borra.
lista.append(elemento): Añade elemento al final de la lista.
lista.insert(i, elemento): Inserta elemento en la posición i.
lista.extend(lista2): Fusiona lista con lista2.
lista.remove(elemento): Elimina la primera vez que aparece elemento.
"""

print('\n','***'*5)

# Diccionario
diccionario = {
    'Clave1': 'valor1',
    'Clave2': 'valor2',
    'Clave3': 'valor3'
}
print('Tipo de objeto: ',type(diccionario), type(diccionario['Clave2']))
print('Objeto completo: ',diccionario)
print('Objeto iterado: ')
for key in diccionario:
    print(key,diccionario.get(key))
""" 
# Operaciones más comúnes
diccionario.get(‘key’): Devuelve el valor que corresponde con la key introducida.
diccionario.pop(‘key’): Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
diccionario.update({‘key’:’valor’}): Inserta una determinada key o actualiza su valor si ya existiera.
«key» in diccionario: Devuelve verdadero (True) o falso (False) si la key (no los valores) existe en el diccionario.
«definicion» in diccionario.values(): Devuelve verdadero (True) o falso (False) si definición existe en el diccionario (no como key).
 """

print('\n','***'*5)

# Lista con diccionarios
lista_diccionarios = [{
        "Clave1": 1,
        "Clave2": "Valor2"
    },
    {
        "Clave3": "Valor3",
        "Clave4": ["Valor4", "Valor5", "Valor6"]
    }
]
print('Tipo de objeto: ',type(lista_diccionarios), type(lista_diccionarios[0]), ' Valor1: ',type(lista_diccionarios[0]['Clave1']),' Valor4: ',type(lista_diccionarios[1]['Clave4']))
print('Objeto completo: ', lista_diccionarios)
print('Objeto iterado: ')

for iter_list in range(len(lista_diccionarios)):
    for key in lista_diccionarios[iter_list]:
        print(key, lista_diccionarios[iter_list][key])

print('\n','***'*5)