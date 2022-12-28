# Lee todo el archivo
file = open('./20_text.txt')
print(file.read())
file.close()

# Leer cada linea. Ideal para archivos pequeños
file = open('./20_text.txt')
print(file.readline())
print(file.readline())
file.close()

# Para abrir el archivo sin necesidad de cerrarlo manualmente se usa comunmente
with open('./20_text.txt') as file:
    for line in file:
        print(line)

# Para escribir el archivo se agrega el parametro 'r+' para tener permisos de lectura y escritura
with open('./20_text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nNueva linea')

# Cuando se usa 'w+' como parametro sobreescribe todo el archivo 