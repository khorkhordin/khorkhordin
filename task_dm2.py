from drawmn import *

def calculate_scale_factors(left_boundary, right_boundary):
    global scale_factor_x, scale_factor_y
    global x0, y0
    scale_factor_x = window_width()/(right_boundary - left_boundary)
    scale_factor_y = scale_factor_x #FIXME
    x0 = -window_width()/2 - left_boundary*scale_factor_x
    y0 = 0 #FIXME

def scale(x, y):
    screen_x = x*scale_factor_x + x0
    screen_y = y*scale_factor_y + y0
    return screen_x, screen_y

def paint_graph(f, a, b, N = 100,
                col = 'black'):
    penup()
    color(col)
    goto(*scale(a, f(a)))
    pendown()
    for i in range(1, N):
        x = a + (b-a)*i/N
        goto(*scale(x, f(x)))
    penup()

def sqr(x):
    return x*x

def hiperbola(x):
    return 1/x

a = -10.1
b = +10
calculate_scale_factors(a, b)
coordinate_lines(x0, y0)
paint_graph(cos, a, b, col = 'red')
paint_graph(sin, a, b, col = 'pink')
paint_graph(tan, a, b, col = 'blue')
paint_graph(hiperbola, a, b, col = 'green')
