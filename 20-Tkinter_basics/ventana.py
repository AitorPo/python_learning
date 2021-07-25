from tkinter import *
import os


class Programa:
    def __init__(self):
        self.title = 'Título de la GUI de prueba de Tkinter'
        self.icon = './images/r2d2.ico'
        self.icon_alt = './20-Tkinter_basics/images/r2d2.ico'
        self.size = '770x470'
        self.resizable = False

    def cargar(self):
        ventana = Tk()

        # creamos una propiedad "sobre la marcha" para asignar la ventana a la clase
        self.ventana = ventana

        ventana.title(self.title)

        # Icono de la ventana => comprobamos si existe con os.path
        ruta_icono_win = os.path.abspath(self.icon)
        # print(ruta_icono_win)

        # Carga de icono desde fuera de la carpeta del programa
        if not os.path.isfile(ruta_icono_win):
            ruta_icono_win = os.path.abspath(self.icon_alt)
        # icono = PhotoImage(file = '/mnt/c/wamp64/www/master_python/20-Tkinter_basics/images/r2d2.png')
        # ventana.iconphoto(False, icono)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono_win)
        texto.pack()

        # Fijamos el tamaño inicial de la ventana
        ventana.geometry(self.size)
        """
            (0, 0) => no se puede redimensionar
            (1, 0) => solo se redimensiona verticalmente
            (0, 1) => solo se redimensiona horizontalmente
            (1, 1) => redimensión completa
        """
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0,0)    


    def anadirTexto(self, text):
        texto = Label(self.ventana, text = text)
        texto.pack()

    def mostrar(self):
        # Método que arranca la ventana. TIENE QUE SER EL ÚLTIMO
        self.ventana.mainloop()    

# Instanciar el programa
programa = Programa()
# primero cargamos la ventana para que se cree la propiedad 'ventana' que hemos definido sobre la marcha
programa.cargar()   
programa.anadirTexto('Hola')
programa.mostrar()     
