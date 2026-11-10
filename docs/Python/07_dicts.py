### Diccionarios ###

my_dict = dict() # Primera forma de definir un diccionario
my_other_dict = {} # Segunda forma de definir un diccionario

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

my_other_dict = {"Nombre":"TU_NOMBRE", "Apellido":"TU_APELLIDO", "Edad":18, 1:"Python"}

my_dict = {
    "Nombre":"TU_NOMBRE",
    "Apellido":"TU_APELLIDO",
    "Edad":18,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.81
    } # Esta forma de definir es para que sea más visual

print(my_other_dict) # {'Nombre': 'TU_NOMBRE', 'Apellido': 'TU_APELLIDO', 'Edad': 18, 1: 'Python'}
print(my_dict) # {'Nombre': 'TU_NOMBRE', 'Apellido': 'TU_APELLIDO', 'Edad': 18, 'Lenguajes': {'Swift', 'Kotlin', 'Python'}, 1: 1.81}

print(len(my_other_dict)) # 4 --> La función len en diccionarios te dice cuantas claves tenés (lo que va antes de :)
print(len(my_dict)) # 5

print(my_dict["Nombre"]) # TU_NOMBRE
print(my_dict["Lenguajes"]) # {'Python', 'Swift', 'Kotlin'}

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"]) # Pedro

print(my_dict[1]) # 1.81

my_dict["Calle"] = "TU_CALLE"
print(my_dict) # {'Nombre': 'Pedro', 'Apellido': 'TU_APELLIDO', 'Edad': 18, 'Lenguajes': {'Swift', 'Python', 'Kotlin'}, 1: 1.81, 'Calle': 'TU_CALLE'}

del my_dict["Calle"]
print(my_dict) # {'Nombre': 'Pedro', 'Apellido': 'TU_APELLIDO', 'Edad': 18, 'Lenguajes': {'Kotlin', 'Python', 'Swift'}, 1: 1.81} --> Elimina el elemento entre []

print("TU_NOMBRE" in my_dict) # False --> En diccionarios se busca por claves no por valor
print("Nombre" in my_dict) # True --> Da verdadero porque Nombre es una clave

print(my_dict.items()) # dict_items([('Nombre', 'Pedro'), ('Apellido', 'TU_APELLIDO'), ('Edad', 18), ('Lenguajes', {'Python', 'Swift', 'Kotlin'}), (1, 1.81)]) --> Retorna claves y valores
print(my_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1]) --> Retorna claves
print(my_dict.values()) # dict_values(['Pedro', 'TU_APELLIDO', 18, {'Python', 'Swift', 'Kotlin'}, 1.81]) --> Retorna valores

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # De esta forma se crea un diccionario sin valores (que se pueden agregar más tarde)
print(my_new_dict) # {'Nombre': None, 1: None, 'Piso': None}

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list) # Otra forma de crear un diccionario sin valores
print(my_new_dict) # {'Nombre': None, 1: None, 'Piso': None}

my_new_dict = dict.fromkeys(my_dict) # Crea un diccionario con las mismas claves que el anterior, pero no con sus valores
print(my_new_dict) # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}
