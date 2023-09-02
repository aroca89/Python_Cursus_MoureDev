### Error Types ###

#SyntaxError
#print "Hola comunidad" # Descomentar para Errror
print("Hola comunidad!")

#NameError
language = "Spanish" # Comentar para Error
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScipt"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) #Descomentar para error

# ModuleNotFoundError
#import maths # Descomentar para Error
import math

# AttributeError
#print(math.PI) # Descomentar para error
print(math.pi)

# KetError
my_dict = {"Nombre":"Aritz", "Apellidos":"Roca", "Edad":34, 1:"Python"}
#print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Edad"])

# TypeError
#print(my_list["0"]) # Descomentar para Error
print(my_list[0])

# ImportError
#from math import PI # Descomentar para Error
from math import pi
print(pi)

# valueError
# my_int = int("10 Años") #Descomentar para Error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
#print(4/0) # Descomentar para Error
print(4/2)

