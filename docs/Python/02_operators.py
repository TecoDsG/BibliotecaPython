### Operadores Aritméticos ###

print(3 + 4) # 7
print(3 - 4) # -1
print(3 * 4) # 12
print(3 / 4) # 0.75
print(10 % 3) # 1 --> Nos dice el resto que queda de la división
print(10 // 3) # 3 --> Nos da la división aproximada a un número entero
print(2 ** 3) # 8 --> Así se hacen las potencias
print(2 ** 3 + 3 - 7 / 1 // 4) # 10.0 --> Se pueden mezclar los distintos operadores

print("Hola " + "Python " + "¿Qué tal?") # Hola Python ¿Qué tal? --> Se puede usar el + para str 

# No se pueden sumar tipos distintos
# print("Hola " + 5) daría error
print("Hola " + str(5)) # Hola 5
print("Hola " * 5) # Hola Hola Hola Hola Hola
print("Hola " * (2 ** 3)) # Hola Hola Hola Hola Hola Hola Hola Hola

my_float = 2.5 * 2
print("Hola " * int(my_float)) # Hola Hola Hola Hola Hola

### Operadores Comparativos ###

print(3 > 4) # False
print(3 < 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
print(3 == 4) # False
print(3 != 4) # True
print(3 > 4 == 2) # False

# Al comparar str, comprueba una ordenación alfabética ASCII
print("Hola" > "Python") # False
print("Hola" < "Python") # True
print("aaaa" >= "abaa") # False
print("Hola" <= "Python") # True
print("Hola" == "Hola") # True
print("Hola" != "Python") # True

# Para comprobar caracteres:
print(len("Hola") > len("Python")) # False
print(len("Hola") < len("Python")) # True
print(len("aaaa") >= len("AAAA")) # True
print(len("Hola") <= len("Python")) # True
print(len("Hola") == len("Hola")) # True
print(len("Hola") != len("Python")) # True

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python") # False
print(3 > 4 or "Hola" > "Python") # False
print(3 < 4 and "Hola" < "Python") # True
print(3 < 4 or "Hola" > "Python") # True
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # True
print(not(3 > 4)) # True