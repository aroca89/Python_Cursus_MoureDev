### Algunos Operators ###

print(10 + 3) #Suma
print(10 - 3) #Resta
print(10 * 3) #Multiplicacion
print(10 / 3) #Division
print(10 % 3) #Resto
print(10 // 3) #Division con aprosimacion a int (Flor division)
print(10 ** 3) #Elevacion
print(10 ** 3 + 3 - 7 / 1 //4) #Podemos mezclar los operadores para realizar operaciones complejas

print("Hola" + " Python") #Concatenacion de cadenas
print("Hola " + str(5)) #No podemos mezclar tipos de datos hay que convertirlos
print("Hola " * 5) #Podemos multiplicar un string o la cantidad de veces que se va a imprimir
print("Hola" * (5 ** 2)) #Podemos hacer operaciones complejas antes de imprimir

my_float = 2.5 * 2 # =5.0 No podemos multiplidcar una cadena por un float,  que este print se repita.
print("float>>", "Hola" * int(my_float)) #por lo que devemos convertirlo a entero para conseguir.

### Operadores Comparativos ###

print(10 > 4)
print(10 < 4)
print(10 >= 4)
print(10 <= 4)
print(10 == 4)
print(10 != 4)
print(10 > 4 == 2) #Podemos mezclar los diferentes operadores

#Podemos ver que al aplicar estos operadores a strings compara la ordenadcion alfabetica segun su valor en la tabla assci

print("Operaciones comperaciones str>>","Hola" < "Python")
print("Operaciones comperaciones str>>","Hola">= "Python")
print("Operaciones comperaciones str>>","Hola" <= "Python")
print("Operaciones comperaciones str>>","Hola"== "Python")
print("Operaciones comperaciones str>>","Hola"!= "Python")
print("Operaciones comperaciones str>>","Hola"> "Python" == "Mundo")

# Ejemplo para que podamos comparar la cantidad de caracteres de un string
print("Comparacion longitud string>>",len("Hola") > len("Python"))
print(len("Hola"), len("Python"))

### Operadores Logicos ###

print(10 > 4 and "Hola" > "Python")#Las dos se deven cumplirse para ser true
print(10 > 4 or "Hola" > "Python")#Con qu se cumpla una  ya seria true
print(10 > 4 or ("Hola" > "Python" and 4 == 4))# Vemos como se puede priorizar unas comparaciones a otras con ()
print(not(10 > 4)) # Not lo que hace es negar la verdad


