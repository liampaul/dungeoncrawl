import math
import sys
import pgzrun
import pygame
import functions
import random
import combat
import setup
from setup import setup, setup_images
from reset import reset_text, reset_pos

#make varibles ______________________________________
for i in range(1):
    #[
    positions = []
    mod = sys.modules['__main__']
    enemy_atk = []
    WIDTH, HEIGHT = 1500, 860
    maxHP = 70
    index = 0

    enemyHP, playerHP = combat.generate_enemy_hp(3), maxHP
    max_enemyHP = enemyHP.copy()

    enemy_atk_power, enemy_block_power = combat.generate_enemy_powers(enemyHP)
    enemy_block_pending, enemy_attack_pending = combat.predict_actions(enemyHP, enemy_block_power, enemy_atk_power)
    player_block, enemy_block = 0, [1 for i in enemyHP]
    selected_count = 0
    toggle_pressed = 0

    # make empty lists
    imagepos, hitboxes, size = [], [], []
    mouse_position = [0, 0]

    skills = ['strike', 'jab', 'defend', 'heal']
    skills_selected = [0 for i in skills]
    selectable = []

    #]
    images = setup_images()
selected, normal_size, in_grid = setup(enemyHP, skills)



def add_image(x, y, image):
    global positions
    positions.append([x, y, image])
    selectable.append(0)


# init pos -----------------------------------------







x = 600
y = 100
# enemy sprite init
for i in range(len(enemyHP)):
    add_image(x, y, 'red')
    x = x + 150
    enemy_block.append(0)

#player and next init
add_image(100, 100, 'idle')
add_image(1000, 500, 'next')

x = 0
y = 612
for i in range(len(skills)):

    add_image(x, y, f"{i}_skill")


    x += 100

#--------------------------------------------------


reset_pos(positions, selected, enemyHP, skills)

# get hitboxes
index = 0
for i in positions:
    hitboxes.append([i[0], i[1]])
    size.append(normal_size[index])

    # add lower corner position
index = 0
for i in hitboxes:
    i.append(i[0] + (normal_size[index][0]))
    i.append(i[1] + (normal_size[index][1]))
    index += 1

for i in skills:
    selectable.append(1)

def game_loop():
    global mouse_position
    global selected_count
    mouse_position = pygame.mouse.get_pos()

    #selected count
    selected_count = 0
    for i in selected:
        if i == 1:
            selected_count += 1




def draw():
    global enemy_block_pending, toggle_pressed, size, selected, player_block, playerHP, positions

    mod.screen.clear()
    index = 0
    functions.draw_image(images['background'], (1500, 860), 0, 0)
    for i in hitboxes:
        if ((mouse_position[0] > i[0] and mouse_position[0] < i[2]) and (
            mouse_position[1] > i[1] and mouse_position[1] < i[3])):
            print(selectable)
            print(index)
            if selectable[index] == 1 and pygame.mouse.get_pressed()[0]:
                print('click')
                if toggle_pressed == 0:
                    if selected[index] == 0 and selected_count < 3:
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
                        if positions[index2][2] == 'red':
                            enemyHP[0] = enemyHP[0] - random.randint(4,8)
                        elif positions[index2][2] == 'blue':
                            player_block += random.randint(4,6)
                        elif positions[index2][2] == 'green':
                            playerHP += random.randint(1, 4)
                            if playerHP > maxHP:
                                playerHP = maxHP

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
        functions.draw_image(images[i[2]], (size[index][0], size[index][1]), i[0], i[1])
        index += 1
    positions = reset_pos(positions, selected, enemyHP, skills)


    index = 0
    x = 600
    y = 100
    for i in enemyHP:
        pygame.draw.rect(mod.screen.surface, (30, 30, 30), (x-27, y + 120, 104, 20), border_radius=10)

        if enemy_block[index] == 0:
            pygame.draw.rect(mod.screen.surface, (0, 140, 0), (x-25, y + 125, enemyHP[index] / max_enemyHP[index] * 100, 10), border_radius=20)

        else:
            pygame.draw.rect(mod.screen.surface, (0, 0, 140), (x - 25, y + 125, enemyHP[index] / max_enemyHP[index] * 100, 10), border_radius=20)

        x += 150
        index += 1

    for i in reset_text(images, enemyHP, enemy_block_pending, enemy_attack_pending, playerHP, player_block, enemy_atk, enemy_block, max_enemyHP):

        functions.draw_image(i[0], None, i[2], i[3])

    x = 0
    y = 612
    for i in skills:
        if selected[index] == 0:
            functions.draw_image(images[f"{i}_skill"], (100, 236), x, y)
        else:
            functions.draw_image(images[f"{i}_skill_selected"], (100, 236), x, y)
        x+=100
clock.schedule_interval(game_loop, 0.000001)
pgzrun.go()
#750
#430