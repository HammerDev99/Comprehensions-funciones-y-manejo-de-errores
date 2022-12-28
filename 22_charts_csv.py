import csv
import matplotlib.pyplot as plt
import pandas as pd

class charts_csv:

    path = './21_data.csv'
    data = []

    def read_csv_dict(self, path):
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

    def get_row(self):
        resp = False
        while resp == False:
            # Permitir ingresar el nombre del pais en vez de un numero
            try: # Controla las excepciones por valores diferentes a numeros
                row = int(input(f'Elija una fila entre 1 y {len(self.data)}: '))
                if row >= 1 and row < len(self.data): # Controla que el valor se encuentre entre el la longitud del csv
                    resp = True
                else:
                    print('Valor incorrecto intente de nuevo 1')
                    resp = False
            except:
                print('Valor incorrecto intente de nuevo 2')
        return row
    
    def get_column(self, row):
        col = input(f'Seleccione una columna entre: {[i for i in self.data]}')
        return col

    def get_data_years(self, country_data):
        years = {}
        for item in country_data:
            if 'Population' in item:
                tupla = { str(item) : float(country_data[item]) } # Error común que no se hace el cambio de tipo de dato str a int para que se reconozcan los numeros
                years.update(tupla)
        years.pop('World Population Percentage')

        # Ordena el diccionario
        sorted_keys = sorted(years.keys())
        sorted_years={}
        for key in sorted_keys:
            sorted_years[key] = years[key]
        return sorted_years

    def plot_bar_chart(self, values, labels):
        fig, ax = plt.subplots() # figura y coordenadas
        ax.bar(labels, values)
        plt.xticks(rotation = 45)
        plt.show()

    def plot_pie_chart(self, values, labels):
        fig, ax = plt.subplots() # figura y coordenadas
        ax.pie(values, labels=labels)
        ax.axis('equal')
        plt.xticks(rotation=90)
        plt.show()

    def solucion1(self):
        # Elección de la fila a graficar
        row = self.get_row()
        country_data = self.data[row] # Diccionario de los datos del país elegido
        print(f'Ha elegido el número {row}, que corresponde al país', country_data['Country/Territory'])

        # Preparación de los datos de fila
        years = self.get_data_years(country_data)
        
        # Graficación de la población por país elegido
        values = years.values() # [years[i] for i in years]
        labels = years.keys() # [i for i in years]
        self.plot_bar_chart(values, labels)

    def solucion2(self):
        # Graficación de columna elegida usando pandas
        df = pd.DataFrame(self.data)
        columns = df.columns.values
        df['World Population Percentage'] = df['World Population Percentage'].astype('float64') # Convertir el tipo de dato
        values = df['World Population Percentage'].to_numpy().tolist()
        labels = df['Country/Territory'].to_numpy().tolist()
        self.plot_pie_chart(values, labels)

    def solucion2_1(self):
        # Graficacion de columna elegida y usando las funciones list, map, y filter de python
        data_v2 = self.data
        data_v2 = list(filter(lambda item : item['Continent'] == 'South America', data_v2)) # Filtro para paises de sur america
        countries = list(map(lambda x: x['Country/Territory'], data_v2))
        percentages = list(map(lambda x: x['World Population Percentage'], data_v2))
        self.plot_pie_chart(percentages, countries)

    def main(self):
        # Lectura del CSV
        self.data = self.read_csv_dict(self.path)
        self.solucion2_1()

if __name__ == '__main__':
    charts_csv = charts_csv()
    charts_csv.main()