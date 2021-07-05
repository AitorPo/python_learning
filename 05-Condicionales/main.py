color = 'Azul';

if color == 'Azul':
    print(f"El color es {color}");
else:
    print(f"El color NO es {color}");    


dia = int(input('Introduce el día de la semana en número'));

if dia == 1:
    print('Lunes');
elif dia == 2: 
    print('Martes');
else:
    print('Es finde');


edadMinima = 18;
edadMaxima = 65;
edadOficial = 17;

if edadOficial >= 18 and edadOficial < 65:
    print('Edad de trabajo');
else:
    print('Muy joven'); 

pais = 'Alemania';

if pais == 'España' or pais == 'México':
    print('Habla hispana');
else: 
    print('No habla hispana');   

if not (pais == 'España' or pais == 'México'):
    print('NO Habla hispana');
else: 
    print('Habla hispana');  