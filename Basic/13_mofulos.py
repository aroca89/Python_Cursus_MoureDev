### Modules ###

""" Que son los modulos??? Lo que a libreria en otros lenguajes como en C, llamar a 
    funciones externas desde mi fichero, de esta manera generamos programs escalables, 
    mas seguros y evitar la replicacion de codigo"""

# import 10_fuctions # la sintaxis del nombre no es correcta para tratarlo como modulo
import modules # Importamos con el nombre del fichero
#from 10_fuctions import sum_two_values # De esta manera importamos unicamente la funcion definida

modules.sum_values(5, 3, 5) # Necesitamos el nombre del modulo y . por delante de la funcion a la que vamos a relaizar la llamada
modules.print_value("Hola Python!")

# Esto es un modulo importado del sistema

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi # Hemos importado solo la funcion
print(pi)

from math import pi as pi_value # Hemos renonbrado el nombre de la funcion para nosotros
print(pi_value)

"""Python tiene modulos ya predefinidos en su sistema para diferentes propositos con funciones ya programadas"""


