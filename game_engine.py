import pgzrun
import visual_setup
import combat
import pygame, functions, random
from  functions import draw_image


print([0,0] == [0,0])
for i in range(1):
    WIDTH, HEIGHT = 1500, 860
    toggle_pressed = 0
    enemyHP = combat.generate_enemy_hp(2)
    skills = ['strike', 'jab', 'defend', 'heal']
    enemy_stagger_count = 0

game_objects, images = visual_setup.create_visuals(enemyHP, skills)




mouse_position = (0, 0)
print(len(game_objects))
animation_queue = [[] for i in game_objects['animated_objects']]


def game_loop():
    global mouse_position
    global enemy_stagger_count
    enemy_stagger_count = 0
    mouse_position = pygame.mouse.get_pos()
    for i in range(len(enemyHP)):
        if game_objects['animated_objects'][i + 1]['frame'][0] == 'stagger':
            enemy_stagger_count += 1
    print(enemy_stagger_count)


def draw():
    global images
    global toggle_pressed
    global animation_queue
    global enemy_stagger_count
    for i in game_objects['flat_objects']:
        draw_image(i[0], (i[1], i[2]), i[3], i[4])

    for i in game_objects['selectable']:

        if i[-1] == 0:
            draw_image(i[0], (i[1], i[2]), i[3], i[4])

        else:
            draw_image(i[5], (i[6], i[7]), i[8], i[9])
        if((i[3] < mouse_position[0] < (i[3] + i[1])) and (
            i[4] < mouse_position[1] < (i[4] + i[2]))):
            if pygame.mouse.get_pressed()[0]:

                if toggle_pressed == 0:
                    if i[-1] == 0:
                        i[-1] = 1
                    else:
                        i[-1] = 0
                    toggle_pressed = 1
            else:
                toggle_pressed = 0

    for i in game_objects['animated_objects']:
        index = i[(i['frame'][0])][(i['frame'][1])]
        if i['queue']:
            if i == game_objects['animated_objects'][0]:
                if enemy_stagger_count == 0:
                    i['frame'][0] = i['queue'][0]
                else:
                    if i['frame'][0] == 'attack':
                        i['frame'][0] = 'idle'
            else:
                i['frame'][0] = i['queue'][0]

        if (pygame.time.get_ticks() - i['last_frame_time']) > index[5]:
            if i['frame'][1] == len(i[i['frame'][0]])-1:
                if i['frame'][0] == 'idle':
                    i['frame'][1] = 0
                else:
                    if i['queue']:
                        del i['queue'][0]
                    i['animation'] = 'idle'
                    i['frame'][0] = 'idle'
                    i['frame'][1] = 0
            else:
                i['frame'][1] += 1
            i['last_frame_time'] = pygame.time.get_ticks()
            if i == game_objects['animated_objects'][0] and i['frame'] == ['attack', 4]:
                game_objects['animated_objects'][1]['queue'].append('stagger')

        draw_image(images[index[0]], (index[1], index[2]), index[3], index[4])


    if game_objects["selectable"][-1][-1] == 1:
        game_objects["selectable"][-1][-1] = 0
        for i in game_objects["selectable"]:
            if i[0] == images["strike_skill"] and i[-1] == 1:
                i[-1] = 0
                game_objects['animated_objects'][0]['frame'] = ['attack', 0]
                game_objects['animated_objects'][0]['queue'].append('attack')
            elif i[0] == images["jab_skill"] and i[-1] == 1:
                i[-1] = 0
                game_objects['animated_objects'][0]['frame'] = ['attack', 0]
                game_objects['animated_objects'][0]['queue'].append('attack')

clock.schedule_interval(game_loop, 0.000001)
pgzrun.go()