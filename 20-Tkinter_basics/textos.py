from tkinter import *

ventana = Tk()
ventana.geometry('500x500')

texto = Label(ventana, text = 'Bienvenido a mi programa')
texto.config(
    fg = 'white',
    bg = '#000000',
    padx = 120,
    pady = 20,
    font = ('Consolas', 12)
)
texto.pack()

texto = Label(ventana, text = 'Soy Aitor Poquet')
texto.config(
    height = 3, # tkinter mide en líneas, no en px
    bg = 'orange',
    cursor = 'circle'
)
texto.pack(anchor = E)


def pruebas(nombre, apellidos, pais):
    return f'Hola {nombre} {apellidos}, veo que eres de {pais}'

# keyword params => para no tener que seguir el orden de los parámetros del método. Solo tenemos que saber el nombre de los mismos
texto = Label(ventana, text = pruebas(apellidos = 'Poquet', pais = 'Valencia', nombre = 'Aitor'))
texto.config(
    bg = 'green'
)
texto.pack()

ventana.mainloop()