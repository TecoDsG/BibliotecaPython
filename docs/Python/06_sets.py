### Sets ###

my_set = set() # Primera forma de definir un set
my_other_set = {} # Segunda forma de definir un set

print(type(my_set)) # <class 'set'>
print(type(my_other_set)) # <class 'dict'> --> Inicialmente es un diccionario

my_other_set = {"Nombre", "Apellido", 18}
print(type(my_other_set)) # <class 'set'> --> Ahora se convierte en un set

print(len(my_other_set)) # 3

my_other_set.add("Apodo")
print(my_other_set) # Un set no es una estructura ordenada --> Siempre imprime los elementos en un orden distinto

my_other_set.add("Apodo") # Un set no admite repetidos
print(my_other_set) # Imprime lo mismo que el anterior print (es aleatorio)

# print(my_other_set[0]) --> TypeError: 'set' object is not subscriptable --> Como no es una estructura ordenada, no se puede llamar a un indice en concreto

print("Nombre" in my_other_set) # True
print("Nombri" in my_other_set) # False

my_other_set.remove("Apellido") # Elimina el elemento que pongas
print(my_other_set) # {'Nombre', 18, 'Apodo'}

my_other_set.clear() # Elimina todos los elementos del set
print(my_other_set) # set()
print(len(my_other_set)) # 0

del my_other_set # Elimina la variable por completo
# print (my_other_set) --> NameError: name 'my_other_set' is not defined --> Ya no existe la variable my_other_set

my_set = {"Nombre", "Apellido", 18}
my_list = list(my_set) # Hacer este tipo de cambio es arriesgado porque no se sabe el orden en el que va a salir la lista
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"} # Lo de adentro son lenguajes de programación

my_new_set = my_set.union(my_other_set) # Une los dos sets
print(my_new_set) # {'Apellido', 18, 'Kotlin', 'Python', 'Nombre', 'Swift'} --> No tiene porque salir siempre así, es para que se vea que se unen
print(my_new_set.union(my_new_set).union(my_set)) # {'Python', 'Nombre', 'Swift', 18, 'Kotlin', 'Apellido'} --> Siguen saliendo los mismos que antes, ya que no se admiten repetidos
print(my_new_set.union({"JavaScript", "C#"})) # {'Swift', 18, 'Nombre', 'Python', 'C#', 'JavaScript', 'Kotlin', 'Apellido'} --> Ahora si los añade porque antes no estaban pero no los guarda en la variable, porque solo lo cambiamos en el print

print(my_new_set.difference(my_set)) # {'Kotlin', 'Swift', 'Python'} --> A my_new_set le saca los elementos de my_set