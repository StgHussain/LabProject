import tkinter as tk

class ControlScript(tk.Tk):

    def __init__(self, *args, **kwargs):
       
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = MainPage(container, self)

        self.frames[MainPage] = frame

        frame.grid(row=0, column =0, sticky = "nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text ="Hologram Generation")
        label.grid(row = 0, padx = 50)

        label = tk.Label(self, text ="Enter number of Beams required")
        label.grid(row = 1, column = 0)

        self.beamNums = {'beam one', "beam two", 'beam three'}

        self.totalBeamNum = tk.StringVar()
        myEntry = tk.Entry(self, textvariable = self.totalBeamNum)
        myEntry.grid(row=1, column=2, padx = 10, pady = 10, sticky = "E")

    #Drop down menu for beam number, set Beam num to the structs and number of beams the user wants
    ############################################################################
        BeamNum = ['Beam 1', 'Beam 2', 'Beam 3']
        self.Beam = tk.StringVar()
        self.Beam.set("Beam Number")
        dropMenu = tk.OptionMenu(self, self.Beam, *BeamNum)
        dropMenu.grid(row = 2, column = 1)
    #Parameters can be stored in self.Beam, can change its variable type
    ############################################################################

    #Drop down menu for beam type for the given beam number
    ############################################################################
        BeamTypes = ['LG Beam', 'HG Beam', 'Bessel']
        self.BeamT = tk.StringVar()
        self.BeamT.set("Beam Type")
        dropMenu = tk.OptionMenu(self, self.BeamT, *BeamTypes)
        dropMenu.grid(row = 3, column = 1)
    ############################################################################

        label = tk.Label(self, text ="P value")
        label.grid(row = 4, column = 0, padx = 30)

        self.pVal = tk.StringVar()
        myEntry = tk.Entry(self, textvariable = self.pVal)
        myEntry.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "E")

    ############################################################################

        label = tk.Label(self, text ="L value")
        label.grid(row = 5, column = 0, padx = 30)

        self.LVal = tk.StringVar()
        myEntry = tk.Entry(self, textvariable = self.pVal)
        myEntry.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = "E")

    ############################################################################

app = ControlScript()
app.mainloop()