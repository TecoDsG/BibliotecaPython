### MANEJO DE EXCEPCIONES ###

number_one = 5
number_two = 1
number_two = "1"

# try - except

try:
    print(number_one + number_two) 
    print("No se ha producido un error")
except: # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# try - except - else

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Si se produce una excepción, esto no se ejecuta
    print("La ejecución continúa correctamente")

# try - except - else - finally

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally: # Se ejecuta siempre
    print("La ejecucíon continúa")

"""
Si se usa un try, el except es obligatorio, 
pero el else y el finally son opcionales
"""

# Excepciones por tipo

try:
    print(number_one + number_two) 
    print("No se ha producido un error")
except ValueError: 
    print("Se ha producido un ValueError")
except TypeError: 
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(number_one + number_two) 
    print("No se ha producido un error")
except TypeError as error: # Agarra el error específico que se pone 
    print(error) # unsupported operand type(s) for +: 'int' and 'str'

try:
    print(number_one + number_two) 
    print("No se ha producido un error")
except ValueError as error: 
    print(error) # En este ejemplo en concreto, este error no pasa, entonces no agarraría nada y el código daría error
except Exception as e: # El exception agarra cualquier tipo de error, a diferencia de uno concreto
    print(e) # unsupported operand type(s) for +: 'int' and 'str'
