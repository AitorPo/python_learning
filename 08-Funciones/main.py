"""
def muestraNombre():
    print('Aitor\nPepe\tAina');

muestraNombre();   

def mostrarTuNombre(nombre, edad):
    print(f'Tu nombre es {str(nombre)}');

    if edad >= 18:
        print(f'Eres mayor de edad');

nombre = str(input('Escribe tu nombre\n'));
edad = int(input('Escribe tu edad\n'));
mostrarTuNombre(nombre, edad);    
"""


def tabla(numero):
    print(f'Tabla de multiplicar del número {numero}')

    for contador in range(11):
        operacion = contador * numero
        print(f'{numero} x {contador} = {operacion}')

    print('\n')


for numeroTabla in range(1, 11):
    tabla(numeroTabla)

# Parámetros opcionales


def getEmpleado(nombre, id=None):
    print("Empleado")
    print(f'Nombre: {nombre}')
    if id != None:
        print(f'ID: {id}')


getEmpleado('Aitor')


def saludame(nombre):
    saludo = f'Hola, saludos {nombre}'

    return saludo


print(saludame('Aitor'))

print('\n')


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


print(calculadora(5, 5))


def getNombre(nombre):
    texto = f'El nombre es: {nombre}'
    return texto


def getApellidos(apellidos):
    texto = f'El apellido es: {apellidos}'
    return texto


def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + '\n' + getApellidos(apellidos)
    return texto

print(getNombre('Aitor'), getApellidos('Poquet Ginestar'));
print(devuelveTodo('Aitor', 'Poquet Ginestar'));

# Función lambda => solo para tareas pequeñas. Se tiene que hacer en una sola línea
dimeElYear = lambda year: f'El año es: {year}';

print(dimeElYear(2222 * 2));


