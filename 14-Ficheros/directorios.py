import os
import shutil

# crear carpeta
if not os.path.isdir('./mi_carpeta'):
    os.mkdir('./mi_carpeta')
else:
    print('Ya existe ese directorio')

# Eliminar carpeta
# os.rmdir('./mi_carpeta')     

# Copiar carpeta
# ruta_absoluta = os.path.abspath('./')
# # print(ruta_absoluta)
# ruta_original = ruta_absoluta + '/mi_carpeta'
# # print(ruta_original)
# ruta_nueva = ruta_absoluta + '/mi_carpeta_NEW'
# print(ruta_nueva)

# shutil.copytree(ruta_original, ruta_nueva)

contenido = os.listdir('./mi_carpeta')
print(contenido)

for fichero in contenido:
    print('Fichero: ' + fichero)
