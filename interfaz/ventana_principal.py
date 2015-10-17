from Tkconstants import CENTER, BOTH, VERTICAL, X, Y
import Tkinter

#http://sebsauvage.net/python/gui/#class

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):

        Tkinter.Tk.__init__(self,parent)

        self.parent = parent
        self.initialize()
        self.minsize(300,300)
        self.geometry("500x500")

    def crear_campo(self, texto_label='', texto_campo='', row=0):
        labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,
                              textvariable=labelVariable,
                              anchor="w",
                              fg="black",
                              bg="white")
        label.pack(fill=Y,pady=100)
        label.grid(column=0,row=row,columnspan=1,sticky='EW')
        labelVariable.set(texto_label)

        entryVariable = Tkinter.StringVar()
        entry = Tkinter.Entry(self,textvariable=entryVariable)
        entry.grid(column=1,row=row)
        entry.pack(fill=Y,pady=100)
        entry.bind("<Return>", self.OnPressEnter)
        entryVariable.set(texto_campo)
        return labelVariable, entryVariable, entry

    def initialize(self):
        self.grid()
        self.labelVariableCedula, self.entryVariableCedula, self.entryCedula = self.crear_campo(u"Ingrese su cedula",
                                                                                                u"CI (sin puntos ni guiones)",
                                                                                                10)
        self.labelVariablePwd, self.entryVariablePwd, self.entryPwd = self.crear_campo(u"Ingrese su constrasena",
                                                                                       u"Contrasena",
                                                                                       12)
        button = Tkinter.Button(self,text=u"Ingresar !",
                                command=self.OnButtonClick)
        button.grid(column=1,row=15)
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="black",bg="white")
        label.grid(column=0,row=3,columnspan=3,sticky='EW')
        self.labelVariable.set(u"Ingrese sus datos")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry(self.geometry())
        self.entryCedula.focus_set()
        self.entryCedula.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        self.labelVariableCedula.set( self.entryVariableCedula.get()+" (You clicked the button)" )
        self.entryCedula.focus_set()
        self.entryCedula.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
        self.entry1.focus_set()
        self.entry1.selection_range(0, Tkinter.END)



if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Elecciones 2015 - Ingrese a la aplicacion')
    app.mainloop()
