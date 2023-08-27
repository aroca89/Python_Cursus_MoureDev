### Higher Order Functions ###

from functools import reduce # Para utilizar la función refuce()
"""
Que es una HOF?
Una función de orden superior (HOF por sus siglas en inglés, 
Higher-Order Function) es una función que puede tomar una o más 
funciones como argumentos y/o devolver una función como resultado. 
En otras palabras, es una función que interactúa con otras funciones, 
ya sea pasándolas como argumentos o utilizando las que devuelve.
"""

# Definición de una función que suma 1 al valor dado
from functools import reduce


def sum_one(value):
   return value + 1

# Definición de una función que suma 5 al valor dado
def sum_five(value):
    return value + 5

# Definición de una función de orden superior que suma dos valores y luego aplica una función a la suma
def sum_two_values_and_add_values(first_value, second_value, f_unction):
    # Suma los dos valores dados
    sum_result = first_value + second_value
    # Aplica la función recibida (f_unction) a la suma de los valores
    return f_unction(sum_result)

# Llamadas a la función de orden superior con diferentes funciones como argumentos
print(sum_two_values_and_add_values(5, 2, sum_one))  # Suma 5 y 2, y luego aplica sum_one
print(sum_two_values_and_add_values(5, 2, sum_five))  # Suma 5 y 2, y luego aplica sum_five
"""
Explicación:

Se definen dos funciones sum_one y sum_five que toman un valor y le suman 1 y 5, respectivamente.
La función sum_two_values_and_add_values toma dos valores y una función como argumentos. Suma los dos valores, luego aplica la función recibida a la suma y devuelve el resultado.
En las llamadas a sum_two_values_and_add_values, se pasa primero la suma de 5 y 2 como argumento y luego se elige entre sum_one y sum_five como la función para aplicar a la suma.
Este ejemplo ilustra cómo las funciones de orden superior pueden recibir funciones como argumentos y manipularlas para realizar tareas específicas.
"""

### Clousers ###

"""
Que es un closure?
Un closure es una función que "recuerda" las variables que estaban 
disponibles en el momento en que fue definida, y puede acceder y utilizar 
esas variables incluso cuando es llamada en un contexto diferente.
"""

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

### Built-in Higher Order Functions ###

"""
Python proporciona algunas funciones de orden superior integradas en su 
biblioteca estándar. Estas funciones te permiten operar sobre iterables 
(como listas, tuplas, conjuntos, etc.)
"""
numbers = [2, 5, 10, 21, 3, 30]

# Map
"""
Aplica una función a cada elemento de un iterable y 
devuelve un objeto map (iterable)
"""

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
"""
Filtra los elementos de un iterable según una función dada 
y devuelve un objeto filter (iterable)
"""

def filter_greater_than_ten(number):
    if number < 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
"""
Aplica una función de forma acumulativa a los elementos de un iterable y devuelve
un único valor. Debes importar esta función desde el módulo functools
"""
numbers = [2, 5, 10, 21, 3, 30]

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))