# High Order Function: Consiste en funciones que reciben por parametro otra función y la misma puede ser lambda
lambda x : x + 2 # Esto es un lambda

def increment(x):
    return x+1

def high_order_function(x, func):
    return x + func(x)

print(high_order_function(5, increment)) # Se envia la funcion como parametro sin los parentesis
# 5 + (5+1)

# Realizar el ejercicio anterior con lambda
increment_v2 = lambda x : x+1
high_order_function_v2 = lambda x,func: x + func(x)
print(high_order_function_v2(5,increment_v2))

# Se puede enviar adicionalmente una lambda como parametro
print(high_order_function_v2(5,lambda x : x + 2))