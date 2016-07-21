from tkinter import *
from random import choice, randint

screen_width = 400
screen_height = 300
class Ball:
    initial_number = 20
    minimal_radius = 15
    maximal_radius = 30
    available_colors = ['red','green','blue']
    def __init__(self):
        """
        Создааю шарик в случайном месте на холсте
        """
        R = randint(Ball.minimal_radius, Ball.maximal_radius)
        x = randint(0,screen_width-1-2*R)
        y = randint(0,screen_height-1-2*R)
        self._R=R
        self._x=x
        self._y=y
        fillcolor = choice(Ball.available_colors)
        self._avatar = canvas.create_oval(x,y,x+2*R,y+2*R,width=1,fill=fillcolor,outline=fillcolor)

        self._vx=randint(-2,2)
        self._vy=randint(-2,2)


def init_game():
    """
    Создаем необходимое количество шариков и пушку
    """
    global balls
    balls = [Ball() for i in range(Ball.initial_number) ]


def init_main_window():
    global root,canvas,scores_text,scores_value
    root = Tk()
    root.title("Пушка")
    scores_value = IntVar()
    canvas = Canvas(root, width=screen_width,height=screen_height,bg="white")
    scores_text=Entry(root,textvariable=scores_value)
    canvas.grid(row=1,column=0,columnspan=3)
    scores_text.grid (row=1,column=2)





if __name__=="__main__":
    init_main_window()
    init_game()
    root.mainloop()