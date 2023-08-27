### List Comprehension ###

my_original_list = [35, 24, 62, 52, 30, 30, 17]

my_list = [i for i in my_original_list]
print(my_list)

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7 ,8 ,9]
print(my_list)

my_range = range(9) #De esta nanera generamos un rango con una funcion
print(list(my_range))

my_list = [i for i in range(9)]
print(my_list)

my_list = [i + 1 for i in range(9)]
print(my_list)

my_list = [i * 2 for i in range(9)]
print(my_list)

my_list = [i * i for i in range(9)]
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in ranga(9)] #Utilizamos una funcion para modificar el valor antes de guardarlo
print(my_list)