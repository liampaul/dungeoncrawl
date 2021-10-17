import random


def reset_text(images, enemyHP, enemy_block_pending, enemy_attack_pending, playerHP, player_block, enemy_atk, enemy_block, max_enemyHP):
    text = []
    x = 600
    y = 100
    for i in range(len(enemyHP)):
        text.append([(images['normal_font'].render(f'{enemyHP[i]} / {max_enemyHP[i]}', True, 'WHITE')), (40, 20), x + 15, y + 125])


        if enemy_block_pending[i] == 0:
            text.append([(images['normal_font'].render(f'{enemy_attack_pending[i]}', True, 'RED')), (50, 50), x + 25, y + 100])
        else:
            text.append([(images['normal_font'].render(f'{enemy_block_pending[i]}', True, 'BLUE')), (50, 50), x - 20, y + 100])

        if enemy_block[i] > 0:
            text.append([(images['normal_font'].render(f'{enemy_block[i]}', True, 'Blue')), (10, 20), x - 50, y + 125])
        x += 150
    text.append([(images['normal_font'].render(f'{playerHP}', True, 'GREEN')), (50, 50), 50, 20])
    text.append([(images['normal_font'].render(f'{player_block}', True, 'BlUE')), (50, 50), 250, 20])

    #make atk and blk


    return text


def reset_pos(positions, selected, enemyHP, skills):

    x = 525
    y = 350
    index = 0

#make enemy sprites
    for i in range(len(enemyHP)):
        positions[index] = [x, y, 'spider_idle']
        x = x + 150
        index += 1
#make singular sprites
    positions[index] = [25, 200, 'idle']
    positions[index + 1] = [1000, 500, 'next']
    index += 2
    x = 0
    y = 612
    for i in skills:
        if selected[index] == 0:
            positions[index] = [x, y, f"{i}_skill"]
        else:
            positions[index] = [x, y, f"{i}_skill_selected"]
        x += 100
        index +=1
    return positions