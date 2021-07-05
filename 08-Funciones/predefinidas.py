nombre = 'Aitor Poquet'

# funciones generales
print(type(nombre))

# detectar el tipado
comprobar = isinstance(nombre, int)
if comprobar:
    print('Esta es string')
else:
    print('No es cadena')

if not isinstance(nombre, float):
    print('No es un número decimal')

# limpiar espacios
frase = '   mi contenido    ';
print(frase);
print(frase.strip());

# eliminar variables
year = 2021;
print(year);
del year;
# print(year);

# comprobar variable vacía
texto = ' ff ';
if len(texto) <= 0:
    print('Variable vacía');
else:
      print('Tiene contenido ' + str(len(texto)));  

# encontrar caracteres
frase = 'La vida es bella';
print(frase.find('vida'));

# reemplazar palabras en un string
nuevaFrase = frase.replace('vida', 'life');
print(nuevaFrase);

# mayús y minús
print(nombre);
print(nombre.lower());
print(nombre.upper());

