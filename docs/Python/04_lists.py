### Listas ###

my_list = list()
my_other_list = []

print(len(my_list)) # 0

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list) # [35, 24, 62, 52, 30, 30, 17]
print(len(my_list)) # 7

my_other_list = [18, 1.81, "Nombre", "Apellido"] # No hace falta que se guarde el mismo tipo de dato en la lista

print(type(my_list)) # <class 'list'>
print(type(my_other_list)) # <class 'list'>

print(my_other_list[0]) # 18
print(my_other_list[1]) # 1.81
print(my_other_list[-1]) # Apellido
print(my_other_list[-3]) # 1.81
print(my_other_list.count("Nombre")) # 1
print(my_list.count(30)) # 2
# print(my_other_list[-5]) --> Esto da un error porque no existe un valor -5, lo mismo pasaría si se pone un 4
# print(my_other_list[4]) --> IndexError: list index out of range

age, height, name, surname = my_other_list
# age, height, name = my_other_list --> ValueError: too many values to unpack (expected 3, got 4)
print(name) # Nombre

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] # Forma muy poco util de asignar nombres a las variables de la lista
print(name)

print(my_list + my_other_list) # [35, 24, 62, 52, 30, 30, 17, 18, 1.81, 'Nombre', 'Apellido']
# print(my_list - my_other_list) TypeError: unsupported operand type(s) for -: 'list' and 'list'
# print(my_list * my_other_list) TypeError: can't multiply sequence by non-int of type 'list'

my_other_list.append("Nombre de la empresa")
print(my_other_list) # [18, 1.81, 'Nombre', 'Apellido', 'Nombre de la empresa']

my_other_list.insert(1, "Color favorito") # [18, 'Color favorito', 1.81, 'Nombre', 'Apellido', 'Nombre de la empresa']
print(my_other_list)

my_other_list[1] = "Otro color favorito" # Cambia el elemento del indice que se elige
print(my_other_list) # [18, 'Otro color favorito', 1.81, 'Nombre', 'Apellido', 'Nombre de la empresa']

my_other_list.remove("Otro color favorito")
print(my_other_list) # [18, 1.81, 'Nombre', 'Apellido', 'Nombre de la empresa']

my_list.remove(30)
print(my_list) # [35, 24, 62, 52, 30, 17]

print(my_list.pop()) # 17 --> El pop elimina por defecto el ultimo elemento de la lista, pero te deja imprimirlo
print(my_list) # [35, 24, 62, 52, 30]


my_pop_element = my_list.pop(2) # Así se puede guardar el último elemento
print(my_pop_element) # 62
print(my_list) # [35, 24, 52, 30]

del my_list[2] # Elimina el elemento en la posición 2
print(my_list) # [35, 24, 30]

my_new_list = my_list.copy() # Copia los datos de la lista en este punto

my_list.clear() # Elimina todos los elementos de la lista
print(my_list) # []
print(my_new_list) # [35, 24, 30]

my_new_list.reverse() # Revierte el orden de la lista
print(my_new_list) # [30, 24, 35]

my_new_list.sort() # Por defecto, como los elementos son int, los ordena de mayor a menor, pero se pueden elegir los parametros
print(my_new_list) # [24, 30, 35]

print(my_new_list[1:3]) # [30, 35] --> Muy parecido al apartado de 'División' en strings

# Usar .remove(), elimina por el valor que le asginaste, en este caso elimino "Color favorito"
# Usar del, elimina por el indice, en este caso elimino el elemento en el indice 2, que era el 52

my_list = "Hola Python" # Cambia el dato a un str, hay que añadirle los [] para que se haga una lista
print(my_list) # Hola Python
print(type(my_list)) # <class 'str'>

