### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " concatenacion " + my_other_string)

my_new_line_string = ">>>Este es un String\ncon salto de linea<<<"
print(my_new_line_string)

my_tap_string = "\tEste es un String con tabulacion"
print(my_tap_string)

my_scape_string = "\\tEste es un String \\n escapado" 
print(my_scape_string)

# Formateo

name, surname, age = "Aritz", "Roca", 33

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))#Para escribir en varios idiomas
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))# Mayor seguridad ya que bloquea los tipos de deatos erroneos
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))#Mala practica y peor eficienci
print(f"Mi nombre es {name} {surname} y mi edad es {age}")# Mejor manera y mas eficiente

# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

# Division 

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)


language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse 

reverse_language = language[::-1]
print(reverse_language)

# Funciones

print(language.capitalize())#
print(language.upper())#Concvertir a mayusculas
print(language.count("t"))#Contar la cantidad de caracteres que contiene del argumento dado
print(language.isnumeric())#Probar si es un numero
print(language.lower())#Poner todo en minusculas
print(language.upper().isupper())#Concatenar funciones

""""Esto son alguanas de las muchas funciones basicas que hay lo mejor es 
eschar un vistazo atoda la documentacion por hacernos una idea de las 
posibilidades que tenemos"""