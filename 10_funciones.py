### Funciones ###

"""Que son las funciones??? Intenta resolver un problema muy concreto y de esa manera podremos llamar a este conjunto de  codigo para resolver de nuevo otra vez este problema concreto"""

print("\nCaso 1:")
def my_function (): # Todo lo tabulado haci la derecha esta dentro de nustra funcion
    print("Esto es una funcion")

my_function ()
my_function ()
my_function ()

print("\nCaso 2:")
def  sum_two_values (first_number, second_number: int): # Lo coje de la misma manera y le da lo mismo que metas un string
    print(first_number + second_number)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(5.4, 7.1)

print("\nCaso 3:")
def  sum_two_values_with_return (first_value, second_value):
    return first_value + second_value 
# Esta funcion por si solo no imprimira nada por pantalla lla que si que esta devolviendo un valor pero no le estamos indicando que lo imprima
my_result = sum_two_values_with_return (10,5) # Primero guardamos el retorno del la funcion ara reusarlo o imprimirlo mas adelante
print(my_result)
print(sum_two_values_with_return (10, 5)) # De esta manera no guardamos el retorno de nuestra funcion directamente lo mostramos en pantalla

print("\nCaso 4:")
def print_name (name, surname):
    print (f"{name} {surname}") # Con la f accedemos a los valores 

print_name(surname = "Roca", name = "Aritz") # Podemos redefinir los parametros en la llamada a la funcion

print("\nCaso 5:")
def print_name_with_default (name, surname, alias = ""): # Podemos dar un valor por defecto a nuestro argumento, asi podremos hacer que siga funcionanando sin pasarle el programa.
    print (f"{name} {surname} {alias}")

print_name_with_default("Aritz", "Roca")

def print_name_with_default (name, surname, alias = ""): 
    print (f"{name} {surname} {alias}")

print_name_with_default("Aritz", "Roca", "aroca-pa")

print("\nCaso 5:")
def print_texts (*texts): # Aplicando el * jeneramos una variable que reciba multiples argumentos
    for text in texts:
        print (text)

print_texts ("hola", "python", "aroca-pa")

print("\nCaso 6:")
def print_upper_texts (*texts): # Funcion con parametros arbitrarios
    print(type(texts)) # Comprobamos el tipo de dato tambien vemos una manera de debugear nuestro codigo 
    for text in texts:
        print (text.upper()) # Podemos aplicar funciones del sistema para consegir quenos lo devuelva como queremos

print_upper_texts ("hola", "python", "aroca-pa")
