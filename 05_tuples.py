### Tuples ###

""" Que es una tupla??? Es una lista inmutable de valores constantes. Una vez inicializada nose pueden anadir ni modificar los elementos """

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (33, 1.77, "Aritz", "Roca")
print(my_tuple)
print(type(my_tuple))

my_other_tuple = (35, 21, 64, 53, 30, 30, 19)
print(my_other_tuple)
print(type(my_other_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# En estos casos funciona de la misma forma que una lista

print(my_tuple.count(33))
print(my_tuple.index(33))

#my_tuple[1] = 1.80
#print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(type(my_sum_tuple))

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) # De esta manera cambiamos el tipo de dato para poder realizar cambios
print(type(my_tuple))

my_tuple[3] = "aroca-pa"
my_tuple.insert(1, "Green")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] # TypeError: 'tuple' object doesn t supoport item deletion

#del my_tuple # No ha limpiado la tupla, lo que a echo es quitar la asignacion o eliminar la variable pero no borra los elementos
#print(my_tuple) # NameError: name 'my_tuple' is not defined





