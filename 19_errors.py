# Existen diferentes tipos de errores dónde el programa se DETIENE: 

#SyntaxError: Eror de sintaxis
""" print('hola')) """

#CeroDivisionError: Division por cero
""" print(0/0) """

#NameError: Variable no inicializada o desconocida 
""" println() """

#AssertionError: Cuando no se da el resultado esperado con la función assert
""" suma = lambda x,y:x+y
assert suma(2,2) == 3 """

# Exception: Generar o lanzar un error manualmente con la palabra reservada raise
""" age = 10
if age < 18:
    raise Exception('No se permite menores de edad') """

# Manejo de errores sin detener el programada. Una buena practica en ingenieria es crear un tracking a los errores presentados
""" try:
    print(0/0)
except ZeroDivisionError:
    print('Error división por cero') """

# Controlar error generado por assert
""" try:
    assert 1!=1,'Uno no es diferente de uno'
except AssertionError as error:
    print(error) """

# Controlar error generado por raise
""" try:
    age = 10
    if age < 18:
        raise Exception('No se permite menores de edad')
except Exception as error:
    print(error) """

# Tambien es posible unificar todos los errores en un solo try indicando todas las posibles excepciones
try:
    print(0/0)
    assert 1!=1,'Uno no es diferente de uno'
    age = 10
    if age < 18:
        raise Exception('No se permite menores de edad')
except ZeroDivisionError as error:
    print(error) # Solo se ejecuta el primer error y se sale del try pero continua con la ejecución de las instrucciones posteriores
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)