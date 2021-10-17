import pygame


def setup(enemyHP, skills):

    # draw enemies
    selected    = [0 for i in range(len(enemyHP))]

    normal_size = [[200, 200] for i in range(len(enemyHP))]
    in_grid     = [0 for i in range(len(enemyHP))]



    #draw player
    selected.append(0)
    normal_size.append([400,400])

    in_grid.append(0)

    #draw next turn
    selected.append(0)
    normal_size.append([75,75])

    in_grid.append(0)

    #draw skills
    for i in skills:
        selected.append(0)
        normal_size.append([100, 236])

        in_grid.append(0)
    return selected,  normal_size, in_grid


#make grid
def make_grid(objects):
    x, y = 50, 500
    output = []
    index = -1
    for i in range(objects):
        index += 1
        if index == 10:
            x = 50
            y = y + (50 + (50 / 4))
            index = 0
        output.append([x, y])
        x = x + (50 + (50 / 4))
    return output


def setup_images():
    images = {
        'next': pygame.image.load('images/next_turn.png').convert_alpha(),
        'normal_font': pygame.font.SysFont(None, 15),
        'idle': pygame.image.load('images/charecter2.png').convert_alpha(),
        'background': pygame.image.load('images/background_game.png').convert_alpha(),
        'spider_idle': pygame.image.load('images/spider_idle1.png').convert_alpha(),
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
    return images

