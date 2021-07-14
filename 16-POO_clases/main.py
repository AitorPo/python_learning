from coche import Coche

carro = Coche('Amarillo', 'Renault', 'Clio', 150, 200, 4)

print(carro.toString())

# Detectar tipado de objeto
if type(carro) == Coche:
    print('Es un objeto Coche')
else:
    print('No es un objeto Coche')    

print(carro.propiedad_publica)  
print(carro.getPrivada())  
