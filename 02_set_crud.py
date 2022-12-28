set_countries = {'col', 'mex', 'bol'}

size  = len(set_countries) # tamano del conjunto
print(size)

print('col' in set_countries) # Existencia de un dato en el conjunto
print('pe' in set_countries)

# Add
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# Update
set_countries.update({'ar', 'pe', 'ecua'})
print(set_countries)

# Remove
set_countries.remove('col')
print(set_countries)
set_countries.remove('ar')
print(set_countries)
#set_countries.remove('arg') # Si el valos no existe se presenta una excepcion sin embargo hay una forma de manejar la excepcion
set_countries.discard('arg')

# Para limpiar todo el conjunto
set_countries.clear()
print(len(set_countries))