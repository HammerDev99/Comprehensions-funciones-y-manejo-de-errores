# Uso de la función map() con Dict
items = [ # Esto es una lista de diccionarios
    {
        'product': 'camisa',
        'price': 100,
    },
    {
        'product': 'pantalones',
        'price': 300,
    },
    {
        'product': 'pantalones 2',
        'price': 200,
    }
]
# El ejercicio es obtener una lista solo con los datos numericos (price)
prices = list(map(lambda item: item['price'], items))
print(prices)
print(items) # No cambia el array original

# Otro ejercicio sería agregar una clave y valor a cada diccionario de la lista
def add_taxes(item):
    new_item = item.copy() # Evita la modificación de la lista original
    new_item['taxes'] = new_item['price'] * .19 # Sin la linea anterior asigna la modificación tanto para items como para new_items
    return new_item
new_items = list(map(add_taxes, items)) # No es posible con una lambda function porque no se puede codificar en una linea el ejercicio y el lambda solo se puede en una linea 
print(items) # Cambia el array original sin la linea 23
print(new_items)

