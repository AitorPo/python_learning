pelicula = 'Batman'

peliculas = ['Batman', 'Spiderman', 'TLOTR']
cantantes = list(('J. Lo', 'Eminem', 'La Raíz'))
years = list(range(2020, 2050))
variada = [False, 'Aitor', 22, 33.3]

print(peliculas)
print(cantantes)
print(years)
print(variada)

print('\n')
print(years[0:10])
print(peliculas[2:])

# añadir
peliculas.append('El Hobbit')
print(peliculas)
"""
nuevaPelicula = ''
while nuevaPelicula != 'parar':
    nuevaPelicula = input('Título de la película:');

    if nuevaPelicula != 'parar':
        peliculas.append(nuevaPelicula);

# recorres lista
for pelicula in peliculas:
    print(f'{peliculas.index(pelicula) + 1} - {pelicula}');
"""

# listas multidimensionales
contactos = [
    ['Aitor',
     'aitor.com'],
    ['Aina',
     'aina.com'],
    ['Frida',
     'frida.com']
]

# print(contactos);
# print(contactos[1][1]);
for contacto in contactos:
    print(contacto[0])

print('\n#### Listado de contactos ####')
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print('Nombre: ' + elemento);
        #print(elemento);
        else:
            print('Email: ' + elemento)        
    print('\n')
