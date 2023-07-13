### Loops o Bucles ###

""" Con los bucles generamos repeticiones, podriamos verlos como if que se repiten asta que se cumple la condicion de este"""

# while
"""El while hace que un codigo ser repita tantas veces en funcion de una condicion"""

my_condition = 0

print("\nCaso while 1:") # En este caso entra en un bucle infinito imprimiendo 0
#while my_condition < 10:
    #print(my_condition)

print("\nCaso while 2:") # En este caso vamos aumentando nuestra condicion para que llege a cumplirse la condicion e imprimira cada una de las vezes que pasa por el print asta cumplirse
while my_condition < 10:
    print(my_condition)
    my_condition += 2

print("\nCaso while 3:") # En python podemos poner un else dentro de la condicion
while my_condition < 10:
    print(my_condition)
#    my_condition += 2
else: # Podriamos ver esto como un seguro que en caso de que no se cumpliera nunca tendria una opcion para que no rompa
    print("Mi condicion es mayor o igual que 10")

print("\nCaso while 4:")
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15 y se detiene")
        break #Se detiene la ejecucion del bucle cuando se cumple
        print("Se ejecuta")
    print(my_condition)

# For
""" Un for se repitira tantas veces como elementos tenemos en el listado 
    Podre ser utilizado en cualquier structura que pueda guardar datos
    Un for itera estructuras
"""

my_list = [35, 21, 64, 53, 30, 30, 19]

print("\nCaso 1 for:")
for element in my_list:
    print(element)

print("\nCaso 2 for:")
for element in my_list:
    print(element)
else:
    print("El bucle for para mi lista a terminado")

print("\nCaso 3 for:")
for element in my_list:
    print(element)
    if element == 64:
        continue # Lo que hacemos con continue es volver a al inicio del for, es ta desaconsejado es mejor colocar una condicion.
    print("Se ejecuta")
else:
    print("El bucle for para mi lista a terminado")




print("La ejecucion continua")