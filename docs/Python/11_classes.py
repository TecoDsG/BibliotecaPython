### CLASES ###

"""
Las clases sirven para definir objetos
que sigan un mismo tipo de características,
como la clase Persona, que los objetos dentro
de esta, tendrán que tener características
de una persona.
"""

class MyEmptyPerson: # Así se define una clase --> Los nombres de las clases se suelen escribir con la primera letra de cada palabra en mayúscula y sin espacios ni _
    pass # Indica al programa que no haga nada y siga ejecutando el código --> Se usa si querés dejar una clase vacía, por si todavía no sabes que poner

print(MyEmptyPerson) # Da igual tiene paréntesis o no para llamarla
print(MyEmptyPerson()) # Los paréntesis son para cuando haya que ponerle valores

class Person:
    def __init__(self, name, surname): # Esto sirve para establecer ciertos valores asociados a Persona (el self es obligatorio)
        self.name = name
        self.surname = surname

"""
my_person = Person()
print(my_person) --> TypeError: Person.__init__() missing 2 required positional arguments: 'name' and 'surname'
"""
my_person = Person("TU_NOMBRE", "TU_APELLIDO")
print(f"{my_person.name} {my_person.surname}") # TU_NOMBRE TU_APELLIDO

class Person:
    def __init__(self, name, surname, apodo = "Sin apodo"): # Otra forma de establecer los valores asociados a Persona (el self sigue siendo obligatorio)
        self.full_name = f"{name} {surname} ({apodo})" # Propiedad pública --> Se puede acceder desde afuera
        self.__name = name # Propiedad privada --> No se puede acceder desde afuera

    def get_name(self): # Para poder llamar a la propiedad privada
        return self.__name

    def walk(self): # Si le pasamos self como parametro, se puede acceder a todo lo que esté dentro del self
        print(f"{self.full_name} está caminando")

my_person = Person("TU_NOMBRE", "TU_APELLIDO")
print(my_person.full_name) # TU_NOMBRE TU_APELLIDO (Sin apodo)
print(my_person.get_name()) # TU_NOMBRE
my_person.walk() # TU_NOMBRE TU_APELLIDO (Sin apodo) está caminando

my_other_person = Person("TU_OTRO_NOMBRE", "TU_OTRO_APELLIDO", "TU_APODO")
print(my_other_person.full_name) # TU_OTRO_NOMBRE TU_OTRO_APELLIDO (TU_APODO)
my_other_person.walk() # TU_OTRO_NOMBRE TU_OTRO_APELLIDO (TU_APODO) está caminando
my_other_person.full_name = "Héctor de León (El loco de los perros)" # Así le cambio el valor a full_name --> Pasó de ser f"{name} {surname} ({apodo})" a "Héctor de León (El loco de los perros)"
print(my_other_person.full_name) # Héctor de León (El loco de los perros)

my_other_person.full_name = 666 # También puede pasar a otro tipo totalmente distinto
print(my_other_person.full_name) # 666