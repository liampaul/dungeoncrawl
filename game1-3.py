import math
import sys
import pgzrun
import pygame
import functions
import random
from setup import setup, make_grid, add_sprite_tags


block = 0
mod = sys.modules['__main__']

WIDTH, HEIGHT = 1500, 860

index = 0

toggle_pressed = 0
red_count, blue_count, green_count = 5, 6, 7
target_size, normal_size = [], []
# "grid"
in_grid = []
# make empty lists
imagepos, positions, hitboxes, size, selected = [], [], [], [], []
enemyHP = [50, 30]
mouse_position = [0, 0]

images = {
    'blue': pygame.image.load('images/blue.png').convert_alpha(),
    'red': pygame.image.load('images/red.png').convert_alpha(),
    'green': pygame.image.load('images/green.png').convert_alpha(),
    'next': pygame.image.load('images/next_turn.png').convert_alpha(),
    'normal_font': pygame.font.SysFont(None, 1000)
}

setup(red_count, blue_count, green_count, selected, target_size, normal_size, enemyHP, in_grid,)



def add_image(x, y, image, ):
    global positions
    positions.append([x, y, image])


# init pos -----------------------------------------
print(make_grid(blue_count + red_count + green_count))


positions = (make_grid(blue_count + red_count + green_count))
positions = (add_sprite_tags(blue_count, red_count, green_count, positions))


x = 600
y = 100
# enemy sprite init
for i in range(len(enemyHP)):
    add_image(x, y, 'red')
    x = x + 150

#player and next init
add_image(100, 100, 'green')
add_image(1000, 500, 'next')
#--------------------------------------------------
print(positions)


def reset_text():
    global text
    text = []
    x = 600
    y = 100
    for i in range(len(enemyHP)):
        text.append([(images['normal_font'].render(f'{enemyHP[i]}', True, 'RED')), (50, 50), x + 25, y - 60])
        x += 150
    return text


def reset_pos():
    x = 50
    y = 500

    global index
    index = -1
    for i in range(blue_count + red_count + green_count):
        index += 1
        if index == 10:
            x = 50
            y = y + (50 + (50 / 4))
            index = 0
        if not selected[i] == 1:
            positions[i][0] = x
            positions[i][1] = y
        x = x + (50 + (50 / 4))

    x = 600
    y = 100
    index = (blue_count + red_count + green_count)

#make enemy sprites
    for i in range(len(enemyHP)):
        positions[index] = [x, y, 'red']
        x = x + 150
        index += 1
#make singular sprites
    positions[index] = [100, 100, 'green']
    positions[index + 1] = [1000, 500, 'next']

reset_pos()



# get hitboxes
index = 0
for i in positions:
    hitboxes.append([i[0], i[1]])
    size.append(int(normal_size[index]))

    # add lower corner position
index = 0
for i in hitboxes:
    i.append(i[0] + (normal_size[index]))
    i.append(i[1] + (normal_size[index]))
    index += 1


def game_loop():
    global mouse_position
    mouse_position = pygame.mouse.get_pos()


def draw():
    global toggle_pressed
    global size
    global selected
    mod.screen.clear()
    index = 0
    for i in hitboxes:
        if ((mouse_position[0] > i[0] and mouse_position[0] < i[2]) and (
            mouse_position[1] > i[1] and mouse_position[1] < i[3])):
            size[index] = size[index] + math.ceil((target_size[index] - size[index]) / 10)
            if not selected[index] == 1:



                positions[index][0] = positions[index][0] - int(((size[index] - normal_size[index]) / 2))
                positions[index][1] = positions[index][1] - int(((size[index] - normal_size[index]) / 2))
            if in_grid[index] == 1 and pygame.mouse.get_pressed()[0] and size[index] == target_size[index]:
                if toggle_pressed == 0:
                    if selected[index] == 0:
                        selected[index] = 1
                    else:
                        selected[index] = 0
                    toggle_pressed = 1
            else:
                toggle_pressed = 0
            if positions[index][2] == 'next' and pygame.mouse.get_pressed()[0]:
                index2 = 0
                for i in selected:
                    if i == 1:
                        print(positions[index2][2])
                        print(positions[index2][2] == 'red')
                        if positions[index2][2] == 'red':
                            print('hit')
                            enemyHP[0] = enemyHP[0] - 5

                    index2 += 1
                selected = []
                for i in positions:
                    selected.append(0)

        else:
            if not selected[index] == 1:
                size[index] = normal_size[index]
        index += 1

    index = 0
    for i in positions:
        functions.draw_image(images[i[2]], (size[index], size[index]), i[0], i[1])
        index += 1
    reset_pos()
    for i in reset_text():
        functions.draw_image(i[0], i[1], i[2], i[3])

clock.schedule_interval(game_loop, 0.000001)
pgzrun.go()
