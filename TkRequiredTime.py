import tkinter

def tkRequiredTime():
    print("In tkReqTime")
    root = tkinter.Tk()
    name = tkinter.StringVar()
    prompt = "Требуемое время достижения совпадения (с):"
    
    tkinter.Label(root, text = prompt, font = 16).pack()
    
    entry = tkinter.Entry(root, textvariable=name, font = 16)
    entry.pack()
    entry.focus_set()
    
    button = tkinter.Button(root, text="OK", command=root.destroy, font = 16)
    button.pack()
    
    root.bind('<Return>', (lambda e, b=button: b.invoke())) 
    
    root.update_idletasks() 
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    rootsize = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = w/2 - rootsize[0]/2
    y = h/2 - rootsize[1]/2
    print(rootsize)
    root.geometry("%dx%d+%d+%d" % (rootsize + (x, y)))
    
    root.mainloop()
    
    print("Done: " + name.get())
    
    return int(name.get()) * 1000
