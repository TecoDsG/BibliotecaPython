### FUNCIONES ###

"""
Las funciones ayudar a resolver dos problemas,
en primer lugar, intentan encapsular una lógica concreta,
es decir, intentan resolver un problema muy concreto que 
nosotros vamos a indicar. Por otra parte, gracias a las funciones,
vamos a poder evitar errores, ya que todo el código dedicado a
resolver un problema muy concreto, va a estar en un único
lugar. Entonces, siempre que se quiera resolver ese problema,
llamaremos a esa función, por lo que no va a haber que duplicar código.
"""

def my_function(): # Así se define una función
    print("Esto es una función.")

my_function() # Así se llama a la función

def sum_two_values(first_value, second_value): # Al llamar a esta función, se requieren dos valores
    print(first_value + second_value)
# sum_two_values() --> TypeError: sum_two_values() missing 2 required positional arguments: 'first_number' and 'second_number'

sum_two_values(5, 7) # 12
sum_two_values("5", "7") # 57
sum_two_values(1.4, 5.2) # 6.6

# sum_two_values(5, 7, 1) --> TypeError: sum_two_values() takes 2 positional arguments but 3 were given

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value 
    return my_sum # El return no sirve para imprimir, pero si para guardar un dato

my_result = sum_two_values_with_return(10, 5) # Acá se le asigna a la función my_result el resultado del return con los dos valores que se le asignaron
print(my_result) # 15

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("TU_NOMBRE", "TU_APELLIDO") # TU_NOMBRE TU_APELLIDO
print_name("TU_APELLIDO", "TU_NOMBRE") # TU_APELLIDO TU_NOMBRE --> Guardo "TU_APELLIDO" como name y "TU_NOMBRE" como surname
print_name(surname="TU_APELLIDO", name="TU_NOMBRE") # TU_NOMBRE TU_APELLIDO --> De esta forma, aunque el orden esté mal, guarda los valores con las variables correctas

def print_name_with_default(name, surname, apodo = "Sin apodo"): # El valor por defecto de apodo es "Sin apodo"
    print(f"{name} {surname} - {apodo}")

print_name_with_default("TU_NOMBRE", "TU_APELLIDO") # TU_NOMBRE TU_APELLIDO - Sin apodo
print_name_with_default("TU_NOMBRE", "TU_APELLIDO", "TU_APODO") # TU_NOMBRE TU_APELLIDO - TU_APODO

def print_text(*text): # El * hace que le puedas pasar todos los valores que quiera de esa variable
        print(text)

print_text("Hola") # ('Hola',)
print_text("Hola", "Python", "Mundo") # ('Hola', 'Python', 'Mundo')

def print_texts(*texts):
    for i in texts: # El for hace que los valores se impriman por separado, en líneas distintas
        print(i)

print_texts("Hola") # Hola
print_texts("Hola", "Python", "Mundo")
"""
Hola
Python
Mundo
"""