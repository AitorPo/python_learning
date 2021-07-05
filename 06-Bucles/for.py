
"""
contador = 0;
resultado = 0;

for contador in range(0,5):
    print(f'Voy por el {contador}');
    resultado += contador;
    print('El resultado es ' + str(resultado));
"""
numeroUsuario = int(input('Número de la tabla de multiplicar'));

if numeroUsuario < 1:
    numeroUsuario = 1;

print(f'### Tabla de multiplicar del número {numeroUsuario} ###');

for numeroTabla in range (1,11):

    if numeroUsuario == 45:
        print('Número inválido');
        break;
        
    print(f'{numeroUsuario} x {numeroTabla} = {numeroUsuario * numeroTabla}');