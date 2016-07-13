import tkinter


def button1_command():...


def print_hello(event):...



def init_main_window():
    global root, button1, button2,label,scale

    root = tkinter.Tk()

    button1 = tkinter.Button(root,text="Button 1", command=button1_command)
    button1.bind("<Button>", print_hello)



    button2 = tkinter.Button(root,text="Button 2")
    button2.bind("<Button>", print_hello)

    variable = tkinter.IntVar(0)
    label = tkinter.Label(root,text=variable)
    scale = tkinter.Scale(root, orient=tkinter.HORIZONTAL, length=300,
            from_=0, to = 100,tickinterval=10, resolution=5,variable=variable)

    text = tkinter.Entry(root,textvariable=variable)

    for obj in button1,button2,label,scale,text:
        obj.pack()
if __name__ ==  "__main__":
    init_main_window()

    root.mainloop()


