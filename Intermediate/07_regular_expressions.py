### Regular Expresions ###

"""Las expresiones regulares, también conocidas como regex o regexp, son patrones de búsqueda 
y manipulación de texto utilizados en informática y procesamiento de texto.
 Estos patrones son una secuencia de caracteres que definen un conjunto de cadenas de texto posibles,
 lo que permite buscar y manipular texto de manera muy poderosa y flexible."""

import re

my_string = "Esta es la leccion 7: Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
print(match.span())
print(match.span())


print(re.match("Esta es la lección", my_other_string))
print(re.match("Esta es la lección", my_string))