"""
contador = 1;

while contador <= 100:
    print(f'Estoy en el número {contador}');
    contador += 1;

print('##################################');
contador = 1;
muestrame = str(0);

while contador <= 100:
    muestrame = muestrame + ', ' + str(contador);
    contador += 1;

print(muestrame);    
"""
numeroUsuario = int(input('Número de la tabla de multiplicar'))

if numeroUsuario < 1:
    numeroUsuario = 1

print(f'### Tabla de multiplicar del número {numeroUsuario}###')
contador = 1
while contador <= 10:
    print(f'{numeroUsuario} x {contador} = {numeroUsuario * contador}')
    contador += 1
else:
    print('Tabla terminada')
