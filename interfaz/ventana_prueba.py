from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Conteo de votos - Ingreso")

mainframe = ttk.Frame(root, padding="100 100 300 300")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

document_entry = ttk.Entry(mainframe, width=40, textvariable=feet)
document_entry.grid(column=2, row=2, sticky=(W, E))
password_entry = ttk.Entry(mainframe, width=40, textvariable=feet)
password_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Ingreso al sistema").grid(column=2, row=1)

ttk.Button(mainframe, text="Ingresar", command=calculate).grid(column=2, row=4, ipadx=20, sticky=W)

ttk.Label(mainframe, text="Documento de identidad").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Contrasena").grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

document_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
