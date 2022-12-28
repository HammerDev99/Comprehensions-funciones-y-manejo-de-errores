# Funciones, argumentos y retornos

def find_element(lenth=1, width=1, depth=1): # Se asigna valores por defecto si no se recibe el parametro
    return lenth*width*depth, width, 'Hola'

result, ancho, texto = find_element(width=10)
print(result)
print(ancho)
print(texto)