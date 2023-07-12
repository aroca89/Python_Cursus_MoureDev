### List ###

"""Una list tine operaciones propias de listas como movimiento de datos, reverse, inyeccion... No es lo mismo que un array
    Sin embargo en la practica se utilizan de manera muy parecida siendo el array mas resrtrictivo y inamobible """

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 21, 64, 53, 30, 30, 19]

print(my_list)
print(len(my_list))

my_other_list = [33, 1.45, "Aritz", "Roca"]

print(type(my_list))
print(type(my_other_list))#Comprobamos que l tipo de dato es una lista y no un array 

print(my_other_list[0])# Manera de aceder a los datos segun su posicion
print(my_other_list[1])
print(my_other_list[-3])# El menos -0 no existe y podemos acceder ala lista hacia atras y haci delante pero no dar la vuelta
print(my_list.count(30))# Cuenta las veces que encuentra un argumernto en la lista

age, height, name, surname, = my_other_list # """De esta manera hemos renonbrado los datos dentro de la lista, de hacerlo son 
print(name)                                 #    necesarios tantos como elementos tiene la lista"""

print(my_list + my_other_list)

my_other_list.append("aroca-pa") # Anadimos el elemento al final de nustra lista
print(my_other_list)

my_other_list.insert(1, "Amarillo") # Insertamos el elemento en una posicion especifica
print(my_other_list)

my_other_list[1] = "Green"
print(my_other_list)

my_other_list.remove("Green") # Eliminamos el primer elemento que conincida con el argumento
print(my_other_list)

print(my_list)
my_list.remove(30)
print(my_list)

my_pop_element = my_list.pop(2) #Guardamos el elemento antes de eliminarlo
print(my_pop_element)
print(my_list)

my_list.pop() # Elimina el ultimo elemento de manera predeterminada
print(my_list)

del my_list[2] # Borra el elemento selecionado
print(my_list)

my_new_list = my_list.copy()
print(my_list)


my_list.clear() # Borra la lista
print(my_list)
print(my_new_list) #Nos a copiado en un punto antes de borrar y ahora es una nueva lista

my_new_list.reverse() # Leda la vuelata a la lista
print(my_new_list)

my_new_list.sort() # Ordena la lista, se puede mandar criterios de ordenacion
print(my_new_list)

print(my_new_list[1:3]) # Pendiente de repasar, hacer revanadas o sublistas!!!!!

my_list = "Hola Python"
print(my_list)
print(type(my_list)) # Hemos pisado la lista y cambiado el tipo de dato devido al tipado devil de python