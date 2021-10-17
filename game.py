import sys
import math
import pgzrun
import pygame

import functions

mod = sys.modules['__main__']

WIDTH = 1500
HEIGHT = 860
target_size = 120
normal_size = 100
mouse_position = pygame.mouse.get_pos()
imagepos = []


def game_loop():
    global mouse_position
    mouse_position = pygame.mouse.get_pos()



def draw():
    mod.screen.clear()
    image = pygame.image.load('images/blue.png').convert_alpha()
    global imagepos
    imagepos = []
    global target_size
    global normal_size
    global size
    if (mouse_position[0] < 200 and mouse_position[0] > 100) and (mouse_position[1] < 200 and mouse_position[1] > 100):
        size = size + math.ceil((target_size - size)/10)
        imagepos = [100 - int(((size - normal_size)/2)), 100 - int(((size - normal_size)/2))]
        print(imagepos)
        print(size)
    else:
        imagepos = [100, 100]
        size = normal_size
    functions.draw_image(image, (size, size), imagepos[0], imagepos[1])


clock.schedule_interval(game_loop, 0.00001)
pgzrun.go()
