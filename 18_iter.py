# Iteración sencilla

for i in range(1,11):
    print(i)

# Iterables que se han manuales desde el código

my_iter = iter(range(1,3)) # La palabra reservada iter al imprimirse da como resultado el objeto
print(my_iter) # Esta linea imprime el rango
print(next(my_iter))# la palabra reservada next ejecuta la iteracion en el rango indicado arrojando como resultado de a una iteración
print(next(my_iter))

# Se puede presentar una excepción cuándo no se conoce la longitud del rango a iterar toda vez que puede generar error
print(next(my_iter))