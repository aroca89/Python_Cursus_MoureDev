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

#os.remove("Intermediate/my_file.txt")

# .json file

import json

json.

