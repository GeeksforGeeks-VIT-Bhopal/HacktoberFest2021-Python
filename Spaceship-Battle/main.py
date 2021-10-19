import pygame
import os
pygame.font.init()
pygame.mixer.init()

w, h = 900, 500
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("SPACESHIP BATTLE")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

B = pygame.Rect(w//2 - 5, 0, 10, h)

hit_sound = pygame.mixer.Sound('Assets/Grenade+1.mp3')
fire_sound = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

health = pygame.font.SysFont('comicsans', 40)
winner = pygame.font.SysFont('comicsans', 100)

fps = 60
vel = 5
bul_vel = 7
bul = 3
s_w, s_h = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (s_w, s_h)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (s_w, s_h)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.jpg')), (w, h))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    win.blit(SPACE, (0, 0))
    pygame.draw.rect(win, BLACK, B)

    red_health_text = health.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    win.blit(red_health_text, (w - red_health_text.get_width() - 10, 10))
    win.blit(yellow_health_text, (10, 10))

    win.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    win.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(win, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(win, YELLOW, bullet)

    pygame.display.update()


def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - vel > 0:  # LEFT
        yellow.x -= vel
    if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < B.x:  # RIGHT
        yellow.x += vel
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0:  # UP
        yellow.y -= vel
    if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.height < h - 15:  # DOWN
        yellow.y += vel


def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - vel > B.x + B.width:  # LEFT
        red.x -= vel
    if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < w:  # RIGHT
        red.x += vel
    if keys_pressed[pygame.K_UP] and red.y - vel > 0:  # UP
        red.y -= vel
    if keys_pressed[pygame.K_DOWN] and red.y + vel + red.height < h - 15:  # DOWN
        red.y += vel


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += bul_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > w:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= bul_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = winner.render(text, 1, WHITE)
    win.blit(draw_text, (w/2 - draw_text.get_width() /
                         2, h/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(700, 300, s_w, s_h)
    yellow = pygame.Rect(100, 300, s_w, s_h)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < bul:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    fire_sound.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < bul:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    fire_sound.play()

            if event.type == RED_HIT:
                red_health -= 1
                hit_sound.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                hit_sound.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()
