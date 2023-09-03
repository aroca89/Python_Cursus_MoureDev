### File Handling  ###

import os 
"""puedes usar el módulo os en Python para realizar operaciones relacionadas con el sistema operativo, 
como manipular archivos y directorios, obtener información del sistema, 
gestionar variables de entorno y más"""

# .txt file
"""
Modo	Descripción
'r'	    Modo de lectura. Abre el archivo en modo de solo lectura.
'w'	    Modo de escritura. Abre el archivo en modo de escritura (sobrescribe el archivo existente).
'a'	    Modo de agregar. Abre el archivo en modo de escritura, pero agrega contenido al final del archivo.
'r+'	Modo de lectura y escritura. Abre el archivo para lectura y escritura.
'w+'	Modo de escritura y lectura. Abre el archivo en modo de escritura y lectura (sobrescribe el archivo existente).
'wb'	Modo de escritura binaria. Abre el archivo en modo de escritura binaria (archivos binarios).
'rb'	Modo de lectura binaria. Abre el archivo en modo de lectura binaria (archivos binarios). 
"""

txt_file = open("Intermediate/my_file.txt", "w+")
txt_file.write("Mi nombre es Aritz\nMi apellido es Roca\n34 años\ny mi lenguaje preferido es python")
#print(txt_file.read()) # Printea todo el archivo
print(txt_file.read(10)) # Printea la cantidad de caracteres dada
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

os.remove("Intermediate/my_file.txt") 

# .json file

import json

json_file = open("Intermediate/my_file.json", "w+")

json_test ={
    "name":"Aritz",
    "surname":"Roca",
    "age":"35",
    "language":["Python", "Swift", "Kotlin"],
    "website":"https://aroca-pa.pa"}

json.dump(json_test, json_file, indent= 4)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))

os.remove("Intermediate/my_file.json") 

# .csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_write = csv.writer(csv_file)
csv_write.writerow(["Name", "Surname", "Age", "Language", "Website"])
csv_write.writerow(["Aritz", "Roca", 34, "Python", "https://aroca-pa.pa"])
csv_write.writerow(["Roswell", "", 2, "Cobol", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

os.remove("Intermediate/my_file.csv")

# .xlsx file

#import xlrd # Debe instalarse el módulo

# .xml file

import xml

