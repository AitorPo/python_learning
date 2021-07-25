from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.geometry('700x500')
ventana.tk.call('wm', 'iconphoto', ventana._w, tk.PhotoImage(file='./images/r2d2.png'))
Label(ventana, text = 'Hola, soy Aitor').pack(anchor = W)

imagen = Image.open('./images/roshi.png')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image = render).pack(anchor = E)

ventana.mainloop()