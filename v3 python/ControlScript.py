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
        label.grid(row = 0, padx = 30)

        label = tk.Label(self, text ="Enter number of Beams required")
        label.grid(row = 1, column = 0)

        self.totalBeamNum = tk.StringVar()
        myEntry = tk.Entry(self, textvariable = self.totalBeamNum)
        myEntry.grid(row=1, column=2, padx = 10, pady = 10, sticky = "E")


app = ControlScript()
app.mainloop()