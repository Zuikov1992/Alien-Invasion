import pygame


with open('config/config.conf', encoding='utf8') as f:
    for line in f:
        if "bullet size" in line:
            dictionary = line.split(' ')
            conf = int(dictionary[-1])
        if "speed bullet" in line:
            dictionary_2 = line.split(' ')
            sb = int(dictionary_2[-1])


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, ship,):
        """Создаем пулю в позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, conf, 18)
        self.color = 200, 150, 100
        self.speed = sb
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)
