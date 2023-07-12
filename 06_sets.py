### Sets ###

""" Que es un set? Un set no es una estructura ordenada, no admite elementos repetidos"""

my_set = set() # Utilizamos una funcion para crear un set
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Nos dice que inicialmente es un diccionario

my_other_set = {"Aritz", "Roca", 33}
print(type(my_other_set)) # Cuando metemos elementos deja de ser de tipo diccionario

print(len(my_other_set))

my_other_set.add("aroca-pa") # Un set no admite elementos repetidos
print(my_other_set) # Un set no es una structura ordenada

print("Aritz" in my_other_set) # De esta manera comprobamos si dentro de nuestro set esiste el elemento
print("Python" in my_other_set)

my_other_set.remove("Aritz") # Podemos borrar elementos
print (my_other_set)

my_other_set.clear() # Con el . vemos las operaciones asociadas  al lenguaje
print(len(my_other_set))

#del my_other_set # del es una operacion del sistema no de los sets
#print(my_other_set) # Clear vacia el set pero del elimina la variable y al intentar acceder: NameError: name 'my_other_set' is not defined

my_set = {35, 21, 64, 53, 30, 30, 19}
my_list = list(list(my_set))
print(my_list)
print(my_list[0]) #En este caso convertir en una lista para manipular el set es un riesgo ya que no savemo nunca en que orden se va a guardar

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
my_new_set = my_set.union(my_other_set.union({"C#", "Javascript"})) # Podemos concatenar funciones y anadir elementos sin almacenarlos en la variable
print(my_new_set)

print(my_new_set.difference(my_set)) # Nos qudamos con la diferencia, los elementos de my_set