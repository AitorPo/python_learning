peliculas = ['Batman', 'Spiderman', 'TLOTR'];
numeros = [1, 2, 5, 8, 9, 3, 6];

print(numeros);

numeros.sort();
print(numeros);

# dar la vuelta
numeros.reverse();
print(numeros);

# añadir elementos
peliculas.append('Iron man'); # añade al final
peliculas.insert(1, 'Como entrenar a tu dragón'); # definimos la posición en la que añadir la peli
print(peliculas);

# eliminar elementos
peliculas.pop(1);
peliculas.remove('TLOTR');
print(peliculas);

# buscar dentro de una lista
print('Batman' in peliculas); # True

# contar elementos
print(len(peliculas));

# cuántas veces aparece un elementos
print(numeros.count(8)); # 1
numeros.append(8);
print(numeros.count(8)); # 2

# conseguir índice
print(peliculas.index('Batman'));

# unir listas
peliculas.extend(numeros);
print(peliculas);




