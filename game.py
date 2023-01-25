import pygame, controls, setings
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from scores import Scores


set = setings.Setings()

with open('config/config.conf', encoding='utf8') as f:
    for line in f:
        if "FPS" in line:
            dictionary = line.split(' ')
            conf = int(dictionary[-1])

# Главный цикл
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((set.width, set.height))
pygame.display.set_caption("Инопланетное вторжение")
pygame.display.set_icon(pygame.image.load('img/fav.png'))
bg_color = (230, 230, 230)
ship = Ship(screen)
bullets = Group()
aliens = Group()
controls.create_army(screen, aliens, set.width, set.height)
stats = Stats()
sc = Scores(screen, stats)

while True:
    controls.events(screen, ship, bullets)  # Управление
    if stats.run_game:
        ship.update_ship()  # Обновление позиции корабля
        controls.update(bg_color, screen, stats, sc, ship, aliens, bullets)
        controls.update_bullets(screen, stats, sc, aliens, bullets, set.width, set.height)
        controls.update_alien(stats, screen, sc, ship, aliens, bullets, set.width, set.height)
        clock.tick(conf)
