import pygame
import sys
from bullet import Bullet
from aliens import Alien


def events(screen, ship, bullets):
    """Управление событиями"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # клавиша нажата
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  # вправо
                ship.mright = True
            if event.key == pygame.K_LEFT:  # влево
                ship.mleft = True
            if event.key == pygame.K_SPACE:  # пробел
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)

        # клавиша отжата
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.mright = False
            if event.key == pygame.K_LEFT:
                ship.mleft = False


def update(bg_color, screen, stats, sc, ship, aliens, bullets):
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.output()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, aliens, bullets, width_scr, height_scr):
    """Удаление пульки за пределом экрана"""
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for alien in collisions.values():
            stats.score += 10 * len(alien)
        sc.image_score()
        check_high_score(stats, sc)
        sc.img_ships()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens, width_scr, height_scr)


def ship_kill(stats, screen, sc, ship, aliens, bullets, width_scr, height_scr):
    """Столкновения пушки с армией"""
    if stats.ship_live > 0:
        stats.ship_live -= 1
        sc.img_ships()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens, width_scr, height_scr)
        ship.create_ship()
        pygame.time.delay(1500)
    else:
        stats.run_game = False
        sys.exit()


def update_alien(stats, screen, sc, ship, aliens, bullets, width_scr, height_scr):
    """Обновление позиции пришельцев"""
    aliens.update()
    sc.img_ships()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_kill(stats, screen, sc, ship, aliens, bullets, width_scr, height_scr)
    alien_check(stats, screen, sc, ship, aliens, bullets, width_scr, height_scr)


def alien_check(stats, screen, sc, ship, aliens, bullets, width_scr, height_scr):
    """Проверка по низу экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_kill(stats, screen, sc,  ship, aliens, bullets, width_scr, height_scr)
            break


def create_army(screen, aliens, width_scr, height_scr):
    """Создание армии"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((width_scr - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((height_scr - 100 - 4 * alien_height) / alien_height)
    for row_number in range(number_alien_y - 2):
        for alien_num in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_num
            alien.y = alien_height + alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            aliens.add(alien)



def check_high_score(stats, sc):
    """Проверка рекорда"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('stats/high_score.txt', 'w') as f:
            f.write((str(stats.high_score)))
