import random
from random import randint


def generate_enemy_hp(enemy_count):

    rand_hp = [20, 70]

    enemy_hp = []
    for i in range(enemy_count):
        enemy_hp.append(randint(rand_hp[0], rand_hp[1]))
    if not rand_hp[1] == rand_hp[0]:

        rand_hp[1] -= 10

    return enemy_hp

def generate_enemy_powers(enemyHP):
    rand_blk = [[1, 4], [11, 18]]
    rand_atk = [[3, 4], [5,   9]]
    enemy_blk_power = []
    enemy_atk_power = []
    for i in range(len(enemyHP)):
        enemy_blk_power.append([randint(rand_blk[0][0], rand_blk[0][1]), randint(rand_blk[1][0], rand_blk[1][1])])
        enemy_atk_power.append([randint(rand_atk[0][0], rand_atk[0][1]), randint(rand_atk[1][0], rand_atk[1][1])])

        if not rand_blk[1][1] == rand_blk[1][0]:
            rand_blk[1][1] -= 1
        if not rand_atk[1][1] == rand_atk[1][0]:
            rand_atk[1][1] += 1

    return enemy_atk_power, enemy_blk_power


def predict_actions(enemyHP, enemy_blk_power, enemy_atk_power):
    enemy_atk = [0 for i in enemyHP]
    enemy_blk = [0 for i in enemyHP]
    for i in range(len(enemyHP)):

        if randint(1, 2) == 1:
            enemy_blk[i] = enemy_blk[i] + randint(enemy_blk_power[i][0], enemy_blk_power[i][1])
        else:
            enemy_atk[i] = enemy_atk[i] + randint(enemy_atk_power[i][0], enemy_atk_power[i][1])

    return enemy_atk, enemy_blk


