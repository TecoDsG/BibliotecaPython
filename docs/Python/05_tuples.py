### Tuplas ###

my_tuple = tuple() # Primera forma de definir una tupla
my_other_tuple = (35, 60, 30) # Segunda forma de definir una tupla (No poner [], ya que eso defina una lista (ver Listas))

my_tuple = (18, 1.81, "Nombre", "Apellido", "Nombre")
print(my_tuple) # (18, 1.81, 'Nombre', 'Apellido', 'Nombre')
print(type(my_tuple)) # <class 'tuple'>

print(my_tuple[0]) # 18
print(my_tuple[-1]) # Apellido
# print(my_tuple[4]) --> IndexError: tuple index out of range
# print(my_tuple[-5]) --> IndexError: tuple index out of range

print(my_tuple.count("Nombre")) # 2 --> Nos dice las veces que aparece el valor que introducimos
print(my_tuple.index("Nombre")) # 2 --> Nos dice el indice del primer valor que introducimos

# my_tuple[1] = 1.80 --> TypeError: 'tuple' object does not support item assignment --> Las tuplas son inmutables (a diferencia de las listas)

my_sum_tuple = my_tuple + my_other_tuple # Aunque sean inmutables, si se pueden sumar
print(my_sum_tuple) # (18, 1.81, 'Nombre', 'Apellido', 'Nombre', 35, 60, 30)

print(my_sum_tuple[3:6]) # ('Apellido', 'Nombre', 35) --> Ver División en strings

my_tuple = list(my_tuple) # De esta forma podes cambiar una tupla a una lista (para poder mutarla)
print(type(my_tuple)) # <class 'list'>

my_tuple[4] = "Nombre de la empresa"
my_tuple.insert(1, "Color favorito")
my_tuple = tuple(my_tuple) # Volver a convertir a tupla (para que sea inmutable), es mejor no hacer esto y definirla bien desde el inicio
print(my_tuple) # (18, 'Color favorito', 1.81, 'Nombre', 'Apellido', 'Nombre de la empresa')
print(type(my_tuple)) # <class 'tuple'>

# del my_tuple[2] --> TypeError: 'tuple' object doesn't support item deletion

del my_tuple # Elimina la variable por completo
# print(my_tuple) --> NameError: name 'my_tuple' is not defined