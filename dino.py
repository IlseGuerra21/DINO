from tkinter import *

root = Tk()

framesNum = 24# Numero de frames que tiene el gif
archivo = "pythonProject\DINO\Dino.gif"

# Lista de todas las imagenes del gif
frames = [PhotoImage(file=archivo, format='gif -index %i' %(i)) for i in range(framesNum)]

def update(ind):
    """ Actualiza la imagen gif """
    frame = frames[ind]
    ind += 1
    if ind == framesNum:
        ind = 0
    label.configure(image=frame)
    root.after(5, update, ind) # Numero que regula la velocidad del gif

label = Label(root)
label.pack()
label.configure(background='white')
root.after(0, update, 0)
root.mainloop()