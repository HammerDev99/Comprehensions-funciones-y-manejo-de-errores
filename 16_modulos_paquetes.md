# Modulos importantes de python

- collections: manejo de listas
- re: regular expresions
- time: time
- sys: sistema operativo

## Punto de entrada de python if '__name__' == '__main__'

El punto de entrada de python permite que el modulo sea ejecutado mediante terminal, adicionalmente, si es ejecutado desde otro archivo o importado se va a poder manipular el objeto. Esto permite la dualidad de poderse ejecutar tanto desde otro archivo si es importado el objeto como un script desde la terminal ejecutando las instrucciones contenidas dentro del punto de entrada

## Manejo de paquetes en python < 3.3

Es necesario definir el archivo clave "__init__.py" para que un paquete pueda ser importado desde otro archivo, para las versiones superiores o iguales a 3.3 no es obligatorio crear el archivo clave.

El archivo __init__.py en versiones superiores se puede usar para aparte de declarar un paquete en versiones anteriores, pero para versiones posteriores se utiliza para inicializar algunas variables o importaciones a ese paquete [así](17_pakages/pkg/__init__.py)

El __init___.py solo se inicializa una sola vez y quedan inicilizadas todas las variables indicadas dentro del módulo.

También se puede usar para definir un namespace como la linea 5 del siguiente [archivo](17_pakages/pkg/__init__.py)
