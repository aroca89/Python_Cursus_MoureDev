### Lambdas ### 

# Que es una lambda?
print("\nUna lambda es una función anónima y pequeña definida en una sola línea.")
print("Se utiliza para tareas simples y no requiere un nombre formal.")
print("En este caso, se han definido lambdas para sumar, multiplicar y realizar operaciones con tres valores.")

# Definición de una lambda que suma dos valores
sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))  # Imprime el resultado de sumar 2 y 4

# Definición de una lambda que multiplica dos valores y le resta 3 al resultado
multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))  # Imprime el resultado de multiplicar 2 y 4, y luego restarle 3

# Definición de una función que devuelve una lambda que suma tres valores
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

# Uso de la función sum_three_values para crear una lambda y luego sumar 2, 4 y 5
result_lambda = sum_three_values(5)  # Crea la lambda que suma 5 al resultado
print(result_lambda(2, 4))  # Imprime el resultado de sumar 2, 4 y 5 utilizando la lambda
