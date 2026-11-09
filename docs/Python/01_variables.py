### Variables ###
# En Python las variables se escriben en minúsculas y las distintas palabras se suelen separar con _

my_string_variable = "Mi String Variable"
print(my_string_variable) # Mi String Variable

my_int_variable = 5
print(my_int_variable) # 5

# Transformar una variable tipo int en una tipo str
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable) # 5
print(type(my_int_to_str_variable)) # <class 'str'>

my_bool_variable = False
print(my_bool_variable) # False

my_float_variable = 1.5
print(my_float_variable) # 1.5

my_complex_variable = 3+1j
print(my_complex_variable) # (3 + 1j)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable) # Mi String Variable 5 False
print("Este es el valor de:", my_int_variable) # Este es el valor de: 5

# Algunas funciones del sistema
print(len(my_string_variable)) # 18 --> Cuenta el número de caracteres de la variable

# Variables en una sola línea. No se recomienda
name, surname, apodo, age = "Nombre", "Apellido", "Apodo", 18
print ("Me llamo: ", name," ", surname, ". Mi edad es: ", age, ". Y mi apodo es: ", apodo, sep="") # Me llamo: Nombre Apellido. Mi edad es: 18. Y mi alias es: Apodo

# Inputs
name = input("¿Cuál es tu nombre? ") # Te pide que pongas tu nombre
age = int(input("¿Cuántos años tenés? ")) # Te pide que pongas tu edad
print(name) # El nombre que pusiste
print(age) # La edad que pusiste

# Cambiamos el tipo
name = 18
age = "Nombre"
print(name) # 18
print(age) # Nombre

# ¿Forzamos el tipo?
address: str = "Mi dirección" # Tipo string
address = 32 # Tipo int
address = True # Tipo bool
address = 1.2 # Tipo float
print(type(address)) # <class 'float'>