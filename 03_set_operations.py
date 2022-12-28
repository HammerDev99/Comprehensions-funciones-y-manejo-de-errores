# Union de conjuntos > Selecciona los elementos en comun de los dos conjuntos
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b) # Se puede hacer la union con los operadores logicos directamente

# Interseccion > Vamos a ver los elementos en comun
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b) # Se puede hacer la union con los operadores logicos directamente

# Diferencia > Selecciona los datos del primer conjunto removiendo los del segundo conjunto
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b) # Se puede hacer la union con los operadores logicos directamente

# Diferencia simetrica > Se hace la union sin los elementos en comun
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b) # Se puede hacer la union con los operadores logicos directamente

# Playground de sets
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set.update(countries, centralAm, northAm, southAm)
print(new_set)