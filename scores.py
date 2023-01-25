import pygame.font
from ship import Ship
from pygame.sprite import Group


class Scores():
    """"""
    def __init__(self, screen, stats):
        """Инициализация очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 35)
        self.image_score()
        self.image_high_score()
        self.img_ships()

    def image_score(self):
        """Текс счета в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (230, 230, 230))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (230, 230, 230))
        self.show_score_rect = self.high_score_image.get_rect()
        self.show_score_rect.centerx = self.screen_rect.centerx
        self.show_score_rect.top = self.screen_rect.top + 20

    def img_ships(self):
        """Количество жизней"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_live):
            ship = Ship(self.screen)
            ship.rect.x = 15 + ship_number * ship.rect.width
            ship.rect.y = 20
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.show_score_rect)
        self.ships.draw(self.screen)

