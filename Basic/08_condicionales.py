### Condicionales ###

""" Que es un condicional?? condiciones que an de cumplirse antes de hacer una funcion"""

my_condition = False # Condicionamos la ejecucion del if al valor que queramos True or False

print("\nCaso 1:")
if my_condition: # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condicion del if")
    
print("\nCaso 2:")        
my_condition = 5 * 2

if my_condition == 10: # Condicionamos la condicion 5 * 2 es 10 True
    print("Se ejecuta la condicion del segundo if")
    
print("\nCaso 3:")
if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10 (else) ")
    
print("\nCaso 4:")    
if my_condition > 10 and my_condition < 20: # Se tienen que cumplir ambas condiciones
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual qu 20 ")
    
    """Podemos ver que en python no es necesario el uso de corchetes en este caso"""
    
    print("NO es necesario los corchetes si esta tabulado esta dentro del else")

print("\nCaso 5:")    
if my_condition > 10 and my_condition < 20: # Siempre se inicia un ciclo de condiciones con if 
    print("Es mayor que 10 y menor que 20")
elif my_condition == 10: # Siempre tiene que tener una condicion
    print("Es igual a 10 (elseif)")
else:
    print("Es menor o igual que 10 o mayor o igual qu 20 ") 
   
print("La ejecucion continua")

print("\nCaso 6 cadena vacia:")
my_string = "Mi cadena de texto" # Un string vacio python lo interpreta como que no tiene valor 0???

if not my_string:
    print("My cadena de texto es vacia")

if my_string == "Mi cadena de texto":
    print("Estas cadenas de texto coinciden")


