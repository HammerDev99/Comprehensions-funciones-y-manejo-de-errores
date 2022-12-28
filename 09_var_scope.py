# Scope = Alcance de las variables: Local scope < Enclosing scope < Global scope < Built in

price=100 # Global scope: se puede usar en el ambito del archivo

def increment():
    price = 200 # Local scope
    price = price + 10 # provoca un error por existir una variable con scope global que interfiere en la definicion del objeto por tanto debe crearse una variable con scope local con el mismo nombre y asignarle un nuevo valor como en la linea anterior
    return price

print(price)
print(increment())