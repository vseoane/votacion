from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Conteo de votos - Pagina Principal")

mainframe = ttk.Frame(root, padding="100 100 300 300")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

ttk.Label(mainframe, text="Elecciones 2015").grid(column=2, row=1)

ttk.Button(mainframe, text="Cerrar mesa", command=calculate).grid(row=2, column=2, ipadx=20, sticky=W)
ttk.Button(mainframe, text="Ver resultados", command=calculate).grid(row=3, column=2, ipadx=20, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', calculate)

root.mainloop()
