class Coche:
    # Atributos
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = int(300)
    caballos = int(500)
    plazas = int(2)

    propiedad_publica = 'Puedes acceder desde donde quieras'
    __propiedad_privada = 'Al poner dos barra-baja al inicio me convierto en private'

    # Constructor
    def __init__(self, color, marca, modelo, velocidad, caballos, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballos = caballos
        self.plazas = plazas
        

    # Métodos
    def getPrivada(self):
        return self.__propiedad_privada

    def acelerar(self):
        self.velocidad +=1

    def frenar(self):
        self.velocidad -= 1

    def getMarca(self):
        return str(self.marca)    

    def getVelocidad(self):
        return str(self.velocidad) 

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def toString(self):
        info = '----- Información del coche -----'
        info += f'\n Marca: {self.getMarca()}'    
        info += f'\n Velocidad: {self.getVelocidad()}'    
        return info


