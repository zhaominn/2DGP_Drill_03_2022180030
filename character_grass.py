from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

hide_lattice()

def run_rectangle():
    print('RECTANGLE') 

def run_circle():
    print('CITCLE')

while(True):
    run_circle()
    run_rectangle() 
    
    
close_canvas()

