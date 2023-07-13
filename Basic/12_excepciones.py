### Excepciones Handling ###

number_one, number_two = 5, 1
number_two = "1"


#if number_two > 3:
    #print(number_one = number_two)
#else:
   #print("No se cumplio")

#if type(number_two) == int: # Estamos convirtiendo el dato en un int
#    print(number_one + number_two)
#else:
#    print("No se cumplio")

#try except

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")

# Try except else

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce ninguna excepcion
    print("La ejecucion continua correctamente")

# try except else finally

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecucion continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecucion continua")
    
# Excepciones por tipo

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError: # Captura errores solo del tipo indicado
    print("Se ha producido un Value Error")
except TypeError: # Podemos poner varios para identificar todos
    print("Se ha producido un Type Error")

# Captura de la informacion del error

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error: # Generamos un objeto error donde almacenar la traza
    print(error)
except Exception as exception: # Si el error no es del tipo que hemos determinado podemos recojer el resto de esta manera mas generica
    print(exception)







