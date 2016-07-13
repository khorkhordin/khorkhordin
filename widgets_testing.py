import tkinter


def paint(event):
    """
    :param event: Событие
    :return: Ничего
    """
    print(event.x, event.y)
    canvas.coords(line,0,0,event.x,event.y)

root = tkinter.Tk()

canvas = tkinter.Canvas(root,background="white",width=400,height=400)
canvas.bind("<Motion>",paint)
canvas.pack()
line=canvas.create_line(0,0,0,0)

root.mainloop()