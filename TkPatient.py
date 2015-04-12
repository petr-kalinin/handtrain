import tkinter

class TkPatient:
    def __init__(self):
        root = tkinter.Tk()
        name = tkinter.StringVar()
        tkinter.Entry(root, textvariable=name).pack()
        
        tkinter.Button(root, text="OK", command=root.destroy).pack()

        root.mainloop()
        
        self.name = name.get()
