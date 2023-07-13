### Clases ###

""" Que son las clases??? Las clases nos otorgan un principio y un fin un objeto"""

class MyEmptyPerson: # Como buena practica las clases las escribiremos con el formato camel
    pass # Este comando hace que si esta clase no tine nada no de error, solo tine sentido a la hora de definir la clase

print(MyEmptyPerson)
print(MyEmptyPerson())

class EmptyPerson:
    def __init__(self,) -> None: # _init es un constructor de clase, no una funcion, en este caso no esta haciendo nada
        pass

print("\nEjemplo 1 una sola clase con dos claves")
class Person:
    def __init__(self, name, surname):
        self.name = name # Con el self.creamos la propiedad dentro de nuestra clase u le asignamos el parametro que queramos
        self.surname = surname
        #pass #Quitamos el pass para que funcione

my_person = Person("Roca", "Aritz")
print(my_person.name)
print(f"{my_person.name} {my_person.surname}")


print("\nEjemplo 2 una sola clase con una clave")
class Person:
    def __init__(self, name, surname):
        self.ful_name = f"{name} {surname}"

my_person = Person("Aritz", "Roca")
print(my_person.ful_name)

print("\nEjemplo 3 funcion dentro de la clase")
""" Una funcion dentro de una clase no tiene que llamar al nombre de su clase sino a self para acceder atodo lo que este guardado ya que ya esta dentro"""
class Person:
    def __init__(self, name, surname, alias = ""):
        self.full_name = f"{name} {surname} {alias}" # Propiedad publica podemos acceder y modificarla
        self.__name = name # De esta manera hacemos que la propiedad se ha privada
        self.__surnaem = surname # las propiedades privadas no las podemos modificar, se puede aceder atraves de  la funcion my_person.get_mame() 
        # Una buena practica seria que todas las propiedades fuesen privadas 
        
    def get_name (self):
        return self.__name 
    
    def walk (self):
        print(f"{self.full_name} Esta caminando")

my_person = Person("Aritz", "Roca", "aroca-pa")
print(my_person.full_name)
#print(my_person.__name) #No nos deja acceder por que es privada
#print(my_person.get_name()) # Podemos verla pero no modificarla
my_person.walk ()

print("\nejemplo 3.1 sin alias y cambiando el valor")
my_other_person = Person("Aritz", "Roca")
my_other_person.full_name = "Hector de Leon (El loco de los perros)" # Vemos que podemos cambiar el valor independientemente de lo que le allamos determinado al constructor de clase
print (my_other_person.full_name)

