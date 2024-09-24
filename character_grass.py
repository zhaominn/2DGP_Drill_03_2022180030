from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

hide_lattice()

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.1)

def run_top():
    print('TOP')
    for y in range(50,550,10):
        draw_boy(750, y)
    pass

def run_left():
    print('LEFT')
    for x in range(750,50,-10):
        draw_boy(x, 550)
    pass

def run_bottom():
    print('BOTTOM')
    for y in range(550,50,-10):
        draw_boy(50, y)
    pass

def run_right():
    print('RIGHT')
    for x in range(50,750,10):
        draw_boy(x, 50)
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_left()
    run_bottom()
    run_right()
    pass


def run_circle():
    print('CIRCLE')
    r, cx, cy = 270, 800 // 2, 600 // 2
    for d in range(0,360):
        x=r*math.cos(math.radians(d))+cx
        y=r*math.sin(math.radians(d))+cy

        draw_boy(x,y)
    pass

def run_triangle():
    print('TRIANGLE')

    pass


while(True):
    #run_circle()
    #run_rectangle()
    run_triangle()
    break
    
close_canvas()

