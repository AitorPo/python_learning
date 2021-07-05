# Varibale global

frase = 'Hola esto es una frase de prueba';

print(frase);

def holaMundo():
    frase = 'Hola mundo desde dentro de la función';
    print(frase);

    year = 2021;
    print(year);

    global website;
    website = 'www.com';
    print('Dentro: ' + website);

    return 'Dato devuelto ' + str(year);

print(holaMundo());
print(website);