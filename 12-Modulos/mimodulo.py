def holaMundo(texto):
    return f'{texto}';

def calculadora(n1, n2, basics=False):
    suma = n1 + n2
    resta = n1 - n2
    multi = n1 * n2
    division = n1 / n2

    cadena = ''

    if basics != False:
        cadena += 'Suma: ' + str(suma)
        cadena += '\n'
        cadena += 'Resta: ' + str(resta)
        cadena += '\n'
        cadena += 'Multiplicación: ' + str(multi)
        cadena += '\n'
        cadena += 'División: ' + str(division)

    print('El parámetro basics está a False')

    return cadena    

def getNombre(nombre):
    texto = f'El nombre es: {nombre}'
    return texto    