import tkinter


def click_ball(event):
    """
    Обработчик событий мышки для игрового холста canvas
    :param event: Событие c координатами клика
    По клику удаляем тот объект, на который указывает мышка

    """
    #
    #(event.x, event.y)

def create_random_ball():
    canvas.create_oval(x,y,x+2*R,y+2*R,width=1,fill=random_color())

def init_ball_catch_game():
    """
    Создаем необходимое для игры количество шариков
    :return:
    """

root = tkinter.Tk()

canvas = tkinter.Canvas(root,background="white",width=400,height=400)
canvas.bind("<Motion>",paint)
canvas.pack()
line=canvas.create_line(0,0,0,0)
for i in range (10):
    canvas.create_oval(i*40,i*40,i*40+10,i*40+10,width=2, fill='green')

root.mainloop()