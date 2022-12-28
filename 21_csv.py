import csv

# Lectura del csv por filas
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print('***' * 5)
            print(row)

# Lectura del csv en lista de diccionarios
def read_csv_dict(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') # Lee cada fila
        header = next(reader) # Selecciona el nombre de cada columna
        data = []
        for row in reader:
            iterable = zip(header, row) # itera en las listas y las une
            country_dict = {key: value for key, value in iterable} # Dict comprehensions
            #print(country_dict)
            data.append(country_dict) # Agrega diccionario a la lista
    return data

if __name__ == '__main__':
    path = './21_data.csv'
    read_csv(path)
    data = read_csv_dict(path)
    print(data[0])
