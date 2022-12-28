# Lambdas: son funciones nos permiten versatilidad a la hora de declarar y cierta sintaxis

def increment(x):
    return x+1
print(increment(10))

# Convertir función anterior en una lambda function, para eso debemos reconocer los parametros de entrada y los de salida
increment_v2 = lambda x : x+1# Asignar la función lambda a una variable
print(increment_v2(20))

# Lambda con dos variables
full_name = lambda name, last_name: f'Full name: {name} \nLast name: {last_name}'
print(full_name('Daniel', 'Arbelaez'))