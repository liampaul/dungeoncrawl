import pygame
import sys

mod = sys.modules['__main__']


def scale_image(image, scale):
    return pygame.transform.scale(image, scale)


def draw_image(image, scale, x, y):
    scaled_image = image
    if scale is not None:
        scaled_image = scale_image(image, scale)
    mod.screen.surface.blit(scaled_image, (x, y), special_flags=pygame.BLEND_ALPHA_SDL2)

