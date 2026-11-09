### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string)) # 9
print(len(my_other_string)) # 14

print(my_string + " " + my_other_string) # Mi String Mi otro String

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un string\\nescapado"
print(my_scape_string)

# Formateo

name, surname, age = "Nombre", "Apellido", 18

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Te asegura de que se imprima lo que se busca
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # No se recomienda porque es más larga y es más fácil equivocarse
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Muy recomendada por su rápidez y te deja ver los datos donde querés que vayas

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a) # p
print(e) # o

# División

language_slice = language[1:3]
print(language_slice) # yt

language_slice = language[1:]
print(language_slice) # ython

language_slice = language[-2]
print(language_slice) # o

language_slice = language[0:6:2]
print(language_slice) # pto

# Reverse

reversed_language = language[::-1]
print(reversed_language) # nohtyp

# Funciones

print(language.capitalize()) # Python
print(language.upper()) # PYTHON
print(language.count("t")) # 1
print(language.lower()) # python
print(language.isnumeric()) # False
print("1".isnumeric()) # True
print(language.upper().isupper()) # True
print(language.lower().isupper()) # False
print(language.startswith("py")) # True
print(language.startswith("Py")) # False