import mimodulo;
from mimodulo import calculadora;
from mimodulo import *;

print(mimodulo.holaMundo('Hola que tal'));
print(calculadora(5, 4, True));
print(getNombre('Aitor'));

# modulo fechas
import datetime;
print(datetime.date.today());

fechaCompleta = datetime.datetime.now();
print(fechaCompleta);

fechaPersonalizada = fechaCompleta.strftime('%d/%m/%Y, %H:%M:%S');
print('Fecha personalizada ' + fechaPersonalizada);

print(datetime.datetime.now().timestamp());
print(datetime.datetime.now().time());

import math;
print('Raíz cuadrada de 10: ' + str(math.sqrt(10)));
print('El número pi: ' + str(math.pi));

import random;
print('Número aleatorio entre 15 y 67: ' + str(random.randint(15, 67)));