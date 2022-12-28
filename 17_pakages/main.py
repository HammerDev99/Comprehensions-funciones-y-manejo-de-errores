# Módulos importados desde pkg
from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())

# Variable inicializada desde __init__.py
import pkg
print(pkg.URL)

# Namespace definida desde __init__.py
print(pkg.mod_1.func_1()) # No funciona correctamente solo funciona si se importan los paquetes indicados en lineas 2 y 3 o si se importan desde el modulo __init__.py
