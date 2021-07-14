from io import open
# gestión de archivos
import os
# obtener path de archivos
import pathlib 
# modificacion de archivos
import shutil 

# Abrir archivo
# Tenemos que poner la ruta exacta del fichero. Si está dentro de la misma carpeta solo con poner el nombre del fichero ya lo crea
archivo = open('fichero.txt', 'a+')
content = os.stat('fichero.txt').st_size
# print(content)

# Si ponemos la ruta absoluta del fichero python siempre lo encontrará. Para ello importamos pathlib
ruta = str(pathlib.Path().absolute()) + '/file.txt'
# print(ruta)
file = open(ruta, 'r+')

# Escribir archivo
file.write('#### Soy un texto escrito desde Python ####\n')

# leer contenido
# contenido = file.read()
# print(contenido)
# Cerrar archivo => deberíamos cerrar el archivo SIEMPRE que acabemos de operar con él
# file.close()

# leer contenido y guardarlo en una lista
lista = file.readlines()
file.close()
# podemos leer el archivo con un simple print
# print(lista)

# podemos recorrer el archivo para leerlo línea a línea y manipularlas a nuestro antojo con un for
for frase in lista:
    if not frase.isnumeric():
        # print('-' + frase.upper())
        lista_frase = frase.split()
        # print(lista_frase)

# Copiar
ruta_original = str(pathlib.Path().absolute()) + '/file.txt'  
ruta_nueva = str(pathlib.Path().absolute()) + '/copy_file.txt' 
ruta_nuevo_directorio = str(pathlib.Path().absolute()) + '/../11-Ejercicios_II/copy_file_from_14-Ficheros.txt'
shutil.copyfile(ruta_original, ruta_nuevo_directorio)

# Mover => Si el fichero existe lo reemplaza con el nuevo nombre que le indiquemos (ruta_nueva)
ruta_original = str(pathlib.Path().absolute()) + '/copy_file.txt'  
ruta_nueva = str(pathlib.Path().absolute()) + '/copy_file_NEW.txt' 
ruta_nuevo_directorio = str(pathlib.Path().absolute()) + '/../11-Ejercicios_II/copy_file_from_14-Ficheros_NEW.txt'
# shutil.move(ruta_nueva, ruta_nuevo_directorio)

# Eliminar
# os.remove(ruta_original)

# Comprobar si existe
print(os.path.abspath('./')) # pintar la ruta absoluta

if(os.path.isfile(os.path.abspath('./') + '/file.txt')):
    print('El fichero existe')
else:
    print('El fichero no existe')    





