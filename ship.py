import pygame
from pygame.sprite import Sprite


with open('config/config.conf', encoding='utf8') as f:
    for line in f:
        if "ship soeed" in line:
            dictionary = line.split(' ')
            sh = float(dictionary[-1])


class Ship(Sprite):

    def __init__(self, screen):
        """Инициализация корабля"""
        super(Ship, self). __init__()
        self.screen = screen  # получаем наш экран
        self.image = pygame.image.load('img/ship.png')  # загружаем риснок
        self.rect = self.image.get_rect()  # получаем графичиский объект №1 "корабль" в качестве прямоугольника
        self.screen_rect = screen.get_rect()  # получаем графичиский объект №2 "экран" в качестве прямоугольника
        self.rect.centerx = self.screen_rect.centerx  # помещаем ГО №1 по центру ГО №2
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom  # помещаем ГО №1 внизу ГО №2
        self.mright = False
        self.mleft = False

    def output(self):
        """Рисует корабль"""
        self.screen.blit(self.image, self.rect)  # метод blit рисут (что, где)

    def update_ship(self):
        """Обновление позиции корабля"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += sh
        if self.mleft and self.rect.left > 0:
            self.center -= sh

        self.rect.centerx = self.center

    def create_ship(self):
        """Hfpvtoftn geire d ybpe"""
        self.center = self.screen_rect.centerx