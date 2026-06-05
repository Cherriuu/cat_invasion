import sys
import pygame
from bullet import Bullet
from mouse import Mouse
from time import sleep

def check_event(cat, ai_settings, screen, bullets, stats, play_button, mouses, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # for every action the user takes (clicking the right arrow, hitting space, etc..)
            sys.exit() # system call to exit the game
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, cat, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, cat)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, mouses, bullets, ai_settings, screen, cat, sb)

def check_play_button(stats, play_button, mouse_x, mouse_y, mouses, bullets, ai_settings, screen, cat, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if (button_clicked and not stats.game_active):
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        mouses.empty()
        bullets.empty()

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_cats()

        create_fleet(ai_settings, screen, cat, mouses)
        cat.center_cat()

def check_keydown_events(event, cat, ai_settings, screen, bullets): # when a user presses a key
    if event.key == pygame.K_RIGHT:
        cat.moving_right = True
    elif event.key == pygame.K_LEFT:
        cat.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(cat, ai_settings, screen, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, cat): # when a user releases a key
    if event.key == pygame.K_RIGHT:
        cat.moving_right = False
    elif event.key == pygame.K_LEFT:
        cat.moving_left = False

def update_screen(ai_settings, screen, cat, mouses, bullets, stats, play_button, sb):
    screen.fill(ai_settings.bg_color) # redraw the screen during each iteration
    cat.blitme()
    mouses.draw(screen)

    sb.show_score()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    if not stats.game_active: #runs while False
        play_button.draw_button()

    pygame.display.flip() # updates the screen to the latest

def update_bullets(mouses, bullets, ai_settings, screen, cat, stats, sb):
    bullets.update()

    for bullet in bullets.copy(): # delete bullets once they go off screen to reduce memory usage
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_mouse_collision(bullets, mouses, screen, ai_settings, cat, stats, sb)

def check_bullet_mouse_collision(bullets, mouses, screen, ai_settings, cat, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, mouses, True, True)

    if collisions:
        for mouses in collisions.values():
            stats.score += ai_settings.mouse_points * len(mouses)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(mouses) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, cat, mouses)

        stats.level += 1
        sb.prep_level()

def fire_bullet(cat, ai_settings, screen, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, cat)
            bullets.add(new_bullet)

def create_fleet(ai_settings, screen, cat, mouses):
    mouse = Mouse(ai_settings, screen)
    number_mouse_x = get_number_mouse(ai_settings, mouse.rect.width)
    number_rows_x = get_number_rows(ai_settings, cat.rect.height, mouse.rect.height)

    for row_number in range(number_rows_x):
        for mouse_number in range(number_mouse_x):
            create_mouse(ai_settings, screen, mouses, mouse_number, row_number)

def get_number_mouse(ai_settings, mouse_width):
    available_space_x = ai_settings.screen_width - 2 * mouse_width
    number_mouse_x = int(available_space_x / (1.5 * mouse_width))
    return number_mouse_x

def get_number_rows(ai_settings, cat_height, mouse_height):
    available_space_y = (ai_settings.screen_height - (3 * mouse_height) - cat_height)
    number_rows = int(available_space_y / (1.5 * mouse_height))
    return number_rows

def create_mouse(ai_settings, screen, mouses, mouse_number, row_number):
    mouse = Mouse(ai_settings, screen)
    mouse_width = mouse.rect.width
    mouse.x = mouse_width + 1.5 * mouse_width * mouse_number
    mouse.rect.x = mouse.x
    mouse.rect.y = mouse.rect.height + 1.5 * mouse.rect.height * row_number
    mouses.add(mouse)

def change_fleet_direction(ai_settings, mouses):
    for mouse in mouses.sprites():
        mouse.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, mouses):
    for mouse in mouses.sprites():
        if mouse.check_edges():
            change_fleet_direction(ai_settings, mouses)
            break

def update_mouses(ai_settings, stats, screen, mouses, cat, bullets, sb):
    check_fleet_edges(ai_settings, mouses)
    mouses.update()

    if pygame.sprite.spritecollideany(cat, mouses):
        print("Mouse down!!!")
        cat_hit(ai_settings, stats, screen, cat, mouses, bullets, sb)
    
    check_mouses_bottom(ai_settings, stats, screen, cat, mouses, bullets, sb)


def cat_hit(ai_settings, stats, screen, cat, mouses, bullets, sb):
    if stats.cats_left > 0:
        stats.cats_left -= 1

        sb.prep_cats()

        mouses.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, cat, mouses)
        cat.center_cat()

        sleep(0.5) # pause
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_mouses_bottom(ai_settings, stats, screen, cat, mouses, bullets, sb):
    screen_rect = screen.get_rect()

    for mouse in mouses.sprites():
        if mouse.rect.bottom >= screen_rect.bottom:
            cat_hit(ai_settings, stats, screen, cat, mouses, bullets, sb)
            break

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()




    



