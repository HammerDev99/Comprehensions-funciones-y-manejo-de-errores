# Reduce: es una función que reduce una lista a un solo valor. 
numbers = [1,2,3,4]
import functools # es necesario importar la función
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

# Para los casos en que sea necesario crear una funcion para la ejecución de comandos, se debe enviar la función y el parametro como un aHigh Order Function

def accum(counter, item):
    print('counter =>',counter)
    print('item =>',item)
    return counter + item

result_v2 = functools.reduce(accum, numbers)
print(result_v2)
