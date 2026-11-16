### BUCLES ###

# While

my_condition = 0

"""
El while ejecuta lo que  se le pone adentro
siempre que se cumpla la condición.


while my_condition <= 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor que 10")

print("La ejecución continúa.")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución.")
        break # Detiene la ejecución del while

    print(my_condition)

print("La ejecución continúa.")
"""
# For

"""
Sirve para iterar
un listado de elementos
y se ejecuta tantas veces como elementos tenga.
"""

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (18, 1.81, "Nombre", "Apellido", "Nombre")

for element in my_tuple:
    print(element)

my_set = {"Nombre", "Apellido", 18}

for element in my_set:
    print(element)

my_dict = {"Nombre":"TU_NOMBRE", "Apellido":"TU_APELLIDO", "Edad":18, 1:"Python"}

for element in my_dict:
    print(element) # Imprime las claves no los valores.
    if element == "Edad":
        break # Hace que se pare el bucle al cumplirse la condición.
else:
    print("El bucle for para mi diccionario ha finalizado.")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue # Hace que se vuelva al principio del for al cumplirse la condición. No se aconseja.
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado.")

print("La ejecución continúa")