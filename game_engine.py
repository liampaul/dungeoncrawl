import pgzrun
import combat
import pygame, functions, random
from  functions import draw_image

print([0,0] == [0,0])
for i in range(1):
    WIDTH, HEIGHT = 1500, 860
    toggle_pressed = 0
    enemyHP = combat.generate_enemy_hp(2)
    skills = ['strike', 'jab', 'defend', 'heal']

images = {
        'next': pygame.image.load('images/next_turn.png').convert_alpha(),
        'normal_font': pygame.font.SysFont(None, 15),
        'idle': pygame.image.load('images/charecter_idle1.png').convert_alpha(),
        'idle2': pygame.image.load('images/charecter_idle2.png').convert_alpha(),
        'background': pygame.image.load('images/background_game.png').convert_alpha(),
        'spider_idle': pygame.image.load('images/spider_idle1.png').convert_alpha(),
        'spider_idle2': pygame.image.load('images/spider_idle2.png').convert_alpha(),
        'heal_skill': pygame.image.load('images/heal_skill.png').convert_alpha(),
        'defend_skill': pygame.image.load('images/defend_skill.png').convert_alpha(),
        'strike_skill': pygame.image.load('images/strike_skill.png').convert_alpha(),
        'jab_skill': pygame.image.load('images/jab_skill.png').convert_alpha(),
        'slice_skill': pygame.image.load('images/slice_skill.png').convert_alpha(),
        'heal_skill_selected': pygame.image.load('images/heal_skill_selected.png').convert_alpha(),
        'defend_skill_selected': pygame.image.load('images/defend_skill_selected.png').convert_alpha(),
        'strike_skill_selected': pygame.image.load('images/strike_skill_selected.png').convert_alpha(),
        'jab_skill_selected': pygame.image.load('images/jab_skill_selected.png').convert_alpha(),
        'slice_skill_selected': pygame.image.load('images/slice_skill_selected.png').convert_alpha(),
    }

game_objects = {
    'flat_objects': [],
    'selectable': [],
    'animated_objects': [],
    'particles': []
}



#animated     {'idle': [flat_object1, flat_object2], 'frame': ['idle', 1] 'last_frame_time'
#selectable   {'normal': [image, x, y, width, height], 'selected': [image, x, y, width, height], 'toggled': 1}

#flat_images
#animated_images
#selectable
#parcticle_engine

print(game_objects['flat_objects'])

def add_flat_object(image, x, y, width, height):
    global images
    game_objects['flat_objects'].append([images[image], x, y, width, height])


def add_selectable_object(image, x, y, width, height, image2, x2, y2, width2, height2):
    global images
    game_objects['selectable'].append([images[image], x, y, width, height, images[image2], x2, y2, width2, height2, 0])


add_flat_object('background', 1500, 860, 0, 0)

x = 500
for i in range(len(enemyHP)):
    game_objects['animated_objects'].append(
        {'idle': [['spider_idle', 112, 88, x, 450, 1000], ['spider_idle2', 112, 88, x, 450, 500],], 'frame': ['idle', 0],'last_frame_time': 600, 'animation': 'idle'})

    x += 150
x = 0
for i in skills:
    add_selectable_object(f"{i}_skill", 100, 236, x, 612, f"{i}_skill_selected", 100, 236, x, 612)
    x += 100


game_objects['animated_objects'].append({'idle': [['idle', 100, 200, 100, 350, 1000], ['idle2', 100, 200, 100, 350, 500], ], 'frame': ['idle', 0], 'last_frame_time': 0, 'animation': 'idle'})


mouse_position = (0, 0)



def game_loop():
    print(pygame.time.get_ticks())
    global mouse_position
    mouse_position = pygame.mouse.get_pos()




def draw():
    global images
    global toggle_pressed
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
        if (pygame.time.get_ticks() - i['last_frame_time']) > index[5]:
            if index == i[i['animation']][-1]:
                i['frame'][1] = 0
            else:
                i['frame'][1] += 1
            i['last_frame_time'] = pygame.time.get_ticks()

        draw_image(images[index[0]], (index[1], index[2]), index[3], index[4])

clock.schedule_interval(game_loop, 0.000001)
pgzrun.go()