import pygame


def create_visuals(enemyHP, skills):
    images = {
        'next': pygame.image.load('images/next_turn.png').convert_alpha(),
        'normal_font': pygame.font.SysFont(None, 15),
        'idle1': pygame.image.load('images/charecter_idle1.png').convert_alpha(),
        'idle2': pygame.image.load('images/charecter_idle2.png').convert_alpha(),
        'idle3': pygame.image.load('images/charecter_idle3.png').convert_alpha(),
        'idle4': pygame.image.load('images/charecter_idle4.png').convert_alpha(),
        'idle5': pygame.image.load('images/charecter_idle5.png').convert_alpha(),
        'idle6': pygame.image.load('images/charecter_idle6.png').convert_alpha(),
        'idle7': pygame.image.load('images/charecter_idle7.png').convert_alpha(),
        'idle8': pygame.image.load('images/charecter_idle8.png').convert_alpha(),
        'idle9': pygame.image.load('images/charecter_idle9.png').convert_alpha(),
        'idle10': pygame.image.load('images/charecter_idle10.png').convert_alpha(),
        'attack1': pygame.image.load('images/charecter_attack1.png').convert_alpha(),
        'attack2': pygame.image.load('images/charecter_attack2.png').convert_alpha(),
        'attack3': pygame.image.load('images/charecter_attack3.png').convert_alpha(),
        'attack4': pygame.image.load('images/charecter_attack4.png').convert_alpha(),
        'attack5': pygame.image.load('images/charecter_attack5.png').convert_alpha(),
        'attack6': pygame.image.load('images/charecter_attack6.png').convert_alpha(),
        'background': pygame.image.load('images/background_game.png').convert_alpha(),
        'spider_idle': pygame.image.load('images/spider_idle1.png').convert_alpha(),
        'spider_idle2': pygame.image.load('images/spider_idle2.png').convert_alpha(),
        'spider_stagger1': pygame.image.load('images/spider_stager1.png').convert_alpha(),
        'spider_stagger2': pygame.image.load('images/spider_stager2.png').convert_alpha(),
        'spider_stagger3': pygame.image.load('images/spider_stager3.png').convert_alpha(),
        'spider_stagger4': pygame.image.load('images/spider_stager4.png').convert_alpha(),
        'spider_stagger5': pygame.image.load('images/spider_stager5.png').convert_alpha(),
        'spider_stagger6': pygame.image.load('images/spider_stager6.png').convert_alpha(),
        'spider_stagger7': pygame.image.load('images/spider_stager7.png').convert_alpha(),
        'spider_stagger8': pygame.image.load('images/spider_stager8.png').convert_alpha(),
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

    game_objects['flat_objects'].append([images['background'], 1500, 860, 0, 0])
    game_objects['animated_objects'].append(
        {'idle': [['idle1', 100, 200, 100, 350, 60], ['idle2', 100, 200, 100, 350, 60],
                  ['idle3', 100, 200, 100, 350, 60], ['idle4', 100, 200, 100, 350, 60],
                  ['idle5', 100, 200, 100, 350, 60], ['idle6', 100, 200, 100, 350, 60],
                  ['idle7', 100, 200, 100, 350, 60], ['idle8', 100, 200, 100, 350, 60],
                  ['idle9', 100, 200, 100, 350, 60], ['idle10', 100, 200, 100, 350, 60], ],
         'attack': [['attack1', 200, 200, 100, 350, 100], ['attack2', 200, 200, 100, 350, 100],
                    ['attack3', 200, 200, 100, 350, 100], ['attack4', 200, 200, 100, 350, 50],
                    ['attack5', 200, 200, 100, 350, 100], ['attack6', 200, 200, 100, 350, 50]],


         'frame': ['idle', 0],
         'last_frame_time': 0, 'queue': []})

    x = 500
    for i in range(len(enemyHP)):
        game_objects['animated_objects'].append(
            {'idle': [['spider_idle', 112, 88, x, 450, 1000], ['spider_idle2', 112, 88, x, 450, 500]],
             'stagger': [['spider_stagger1', 152, 116, x, 450, 100], ['spider_stagger2', 152, 116, x, 450, 100],
                         ['spider_stagger3', 152, 116, x, 450, 100], ['spider_stagger4', 152, 116, x, 450, 100],
                         ['spider_stagger5', 152, 116, x, 450, 100], ['spider_stagger6', 152, 116, x, 450, 300],
                         ['spider_stagger7', 152, 116, x, 450, 300], ['spider_stagger8', 152, 116, x, 450, 300]],
             'frame': ['idle', 0], 'last_frame_time': 600, 'queue': []})

        x += 150
    x = 0
    for i in skills:
        game_objects['selectable'].append(
            [images[f"{i}_skill"], 100, 236, x, 612, images[f"{i}_skill_selected"], 100, 236, x, 612, 0])
        x += 100

    game_objects['selectable'].append([images["next"], 150, 100, 700, 612, images['next'], 150, 100, 700, 612, 0])

    return game_objects, images
