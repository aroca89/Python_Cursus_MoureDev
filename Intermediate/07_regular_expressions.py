### Regular Expresions ###
# PROFUNCIZAR CON CALMA SOBRE LAS EXPREONES REGULARES!!!
"""Las expresiones regulares, también conocidas como regex o regexp, son patrones de búsqueda 
y manipulación de texto utilizados en informática y procesamiento de texto.
 Estos patrones son una secuencia de caracteres que definen un conjunto de cadenas de texto posibles,
 lo que permite buscar y manipular texto de manera muy poderosa y flexible."""

from ast import pattern
import re

my_string = "Esta es la lección número 7:\nLección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])


match = re.match("lección", my_other_string)
#if not(match == None): # Otras formas de comprobar en None
#if match != None:
if match is not None:
	print(match)
	start, end = match.span()
	print(my_string[start:end])

#print(re.match("Expresiones Regulares", my_string))

# search

search = re.search("Esta es la lección número 7", my_string, re.I)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)

print(findall)

# split

print(re.split("\n", my_string))

# sub

print(re.sub("Expresiones Regulares", "Regex", my_string, re.I))
print(re.sub("lección|Lección", "LECCION", my_string, re.I))
print(re.sub("[l|L]ección", "LECCION", my_string, re.I))

# Patterns
# Para aprender y validar expresiones regulares www.regex101.com

pattern = r"[l|L]ección"
print(re.findall(pattern, my_string))
pattern = r"[l|L]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

# email validation regular expresion (regex) 
	# https://www.w3resource.com/pyton-exercises/re/python-re-exercise-40.php

def is_valid_email(email):
	pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.+$]"
	return re.match(pattern, email)

email = "arocapazos@gmail.com"
print(is_valid_email(email))

