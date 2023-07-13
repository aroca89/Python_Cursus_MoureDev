### Variables ###

#buena practicas segun PYTHON todo en minusculas y con "_"

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#En esta linea vemos como pasar multiples argumentos a un PRINT()
print(my_bool_variable, my_string_variable, my_int_variable)

#En cierta manere casteamos la variable int para convertirla en un str, o metemos el int dentro de un str
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable, type(my_int_to_str_variable))
#print(type(my_int_to_str_variable))

#Tipo no type (es una funcion)
print(type(print(my_bool_variable, my_string_variable, my_int_variable)))
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print("Esto el la cantidad de caracteres:", len(my_string_variable))

# Variables en una solo linea.    Cuidado con el abuso de esta sintaxis!
name, surname, alias, age = "Aritz", "Roca", 'aroca-pa', 34
print("Me llamo", name, surname, ". Mi edad es:", age, ". Y mi alias", alias, ".")

# Inputs
"""""
name = input('Cual es tu nombre?')
age = input('Cuantos anos tienes?')

print(name)
print(age)
"""""
# Cambiamos su tipo (no tiene un tipado fuerte)
''' Esto proboca que sin darnos cuenta podamos cambiar el tipo de dato inicial o para el que estaba inicialmente penseda esta variable sin darnos cuenta y probocando fallas en nuestro codigo'''

name = 34
age = "Aritz"

print(name)
print(age)

# Forzamos el tipo
"""
En al practica vemos que forzando el typo no lo consegimos y vemos como se a cambiado devido al tipado devil de python, definiendo el tipo de la variable visualmente nos ayuda a saber cual era la idea principal tambien se podria configurar el ide para que nos avise si cambiamos este tipo
"""
address: str = "Mi direccion"
address = 32
print(address)
print(type(address))