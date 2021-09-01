import math
from numpy import array as a
import pygame


class Screen:
    def __init__(self, width: float, height: float, screen_size: a):
        pygame.init()

        self.width = width
        self.height = height
        self.size = a([float(width), float(height)])
        self.screen_size = a(screen_size)
        self.matrix = a([
            [screen_size[0] / width, 0],
            [0, screen_size[1] / height]
        ])
        self.pd = abs(self.matrix[0, 0] * self.matrix[1, 1])  # positive determinant
        self.pd_ = math.sqrt(self.pd)

        self.s_ = pygame.Surface([width, height])
        self.s = pygame.display.set_mode(screen_size)

        self.center = a([width, height]) / 2

    def save(self, path, size=None):
        if size is None:
            pygame.image.save(self.s, path)
        else:
            surface = pygame.Surface(size)

            surface.blit(self.s, [0, 0])

            pygame.image.save(surface, path)
