### Diccionaries ###

""" Que es un diccionario?? Es una forma de al macenar datos asocidos a claves (clave:valor)
    Lo que modelamos en un diccionario es lo que luego conocemos como json??? Como???
"""

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Aritz", "Apellido":"Roca", "Edad":33, 1:"Python"}
my_dict = {
    "Nombre":"Aritz", 
    "Apellido":"Roca", 
    "Edad":33,
    "Lenguajes": {"Python", "swift", "Kotlin"},
    1:1.64
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"]) # De esta manera rescuperamos el valor de la clave

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle aroca-pa"
print(my_dict)

del my_dict["Calle"] # Con del en este caso borramos elementos en vez de la variable my_dict como ocurria en las otras estructuras
print(my_dict)

print("Moure" in my_dict) # Es falso ya que devemos buscar por la clave no por el valor
print("Nombre" in my_dict)

print(my_dict.items()) # Nos retorna todo agrupado por objetos
print(my_dict.keys()) # NOs retorna solo las Claves
print(my_dict.values()) # Nos retorna todos los valores

print("\nCase: 1")
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
print(type(my_new_dict))

print("\nCase: 2")
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Hace una copia de las claves de otro diccionario sele puede dar valores pero no los guarda, no es muy habitual 
print(my_new_dict)
print(type(my_new_dict))

print("\nCase: 3")
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
print(type(my_new_dict))

print("\nCase: 4")
my_new_dict = dict.fromkeys(my_dict, ["Aritz", "Roca"]) # De esta manera damos un valor generico a todas las claves
print(my_new_dict)
print(type(my_new_dict))

""" Estas conversiones en cual quier otro leguaje fuertemente tipado fallaria"""
print(my_new_dict.values()) # De esta menera genero imrimo los valores
print(list(my_new_dict.values())) # De esta manera hacemos una lista de los valore
print(tuple(my_new_dict)) # De esta manera hacemos una lista una tupla o un set de las claves
print(set(my_new_dict))
