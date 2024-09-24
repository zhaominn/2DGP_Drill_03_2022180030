from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

hide_lattice()

def run_rectangle():
    pass

def run_circle():
    pass

while(True):
    run_rectangle() 
    run_circle()
    
close_canvas()

#뼈대를 잡으려면 함수를 써야 한다.(상향식 설계)
#실행 가능한 아주 짧은 코드(틀)을 먼저 작성한다.
