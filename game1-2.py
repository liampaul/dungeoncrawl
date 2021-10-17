import math
import sys

import pgzrun
import pygame

import functions

mod = sys.modules['__main__']

startx = 50
starty = 50

x = startx
y = starty

WIDTH = 1500

HEIGHT = 860
target_size = 150
normal_size = 100
mouse_position = pygame.mouse.get_pos()
imagepos = []
positions = []
objects = [1, 2, 3, 4, 5, ]
hitboxes = []
size = []


# get pos
def reset_pos():
    x = 50
    y = 50
    positions.clear()
    for index in objects:
        positions.append([x, y])
        x = x + (normal_size + (normal_size / 4))


reset_pos()
# get hitboxes
# copy list



print(positions)
print(hitboxes)


def game_loop():
    global mouse_position
    mouse_position = pygame.mouse.get_pos()
    print(mouse_position)
    print(positions)


def draw():
    global size
    mod.screen.clear()
    image = pygame.image.load('images/red.png').convert_alpha()
    index = 0
    for i in hitboxes:
        if (mouse_position[0] > i[0] and mouse_position[0] < i[2]) and (
            mouse_position[1] > i[1] and mouse_position[1] < i[3]):
            print('Adjusting size')
            size[index] = size[index] + math.ceil((target_size - size[index]) / 10)
            positions[index][0] = positions[index][0] - int(((size[index] - normal_size) / 2))
            positions[index][1] = positions[index][1] - int(((size[index] - normal_size) / 2))
        else:
            size[index] = normal_size
        index += 1

    index = 0
    for i in positions:
        functions.draw_image(image, (size[index], size[index]), i[0], i[1])
        index += 1
    reset_pos()

clock.schedule_interval(game_loop, 0.001)
pgzrun.go()
