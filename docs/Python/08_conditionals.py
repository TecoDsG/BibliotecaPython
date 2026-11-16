### Condicionales ###

my_condition = True

if my_condition: # Es lo mismo que poner if my_condition == True: 
    print("Se ejecuta la condición del if")

my_condition = 5 * 3

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

if my_condition > 10 and my_condition < 20: # De esta forma se pueden tener más de una condición
    print("Es mayor que 10 y menor que 20")
elif my_condition == 10:
    print("Es igual a 10")
elif my_condition == 20:
    print("Es igual a 20")
else:
    print("Es menor que 10 o mayor que 20")

print("La ejecución continua")