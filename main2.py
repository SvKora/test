import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

screen = width, heigth =800, 600

BLACK=0, 0, 0
WHITE=255, 255, 255
BLUE= 128,166, 255
YELLOW=255, 255, 0
RED=255, 0, 0
main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(YELLOW)
ball_rect=ball.get_rect()
ball_speed = 1

def create_enemy():
    enemy = pygame.Surface((30, 30))
    enemy.fill(RED)
    enemy_rect = pygame.Rect(width, 100, *enemy.get_size())
    enemy_speed=1
    return [enemy, enemy_rect, enemy_speed]

CREATE_ENEMY =pygame.USEREVENT+1
pygame.time.set_timer(CREATE_ENEMY, 1500)

enemies =[]

is_working = True

while is_working:

    for event in pygame.event.get():
        if event.type == QUIT:
           is_working = False

        if event.type == CREATE_ENEMY:
           enemies.append(create_enemy())
    
    

    pressed_keys = pygame.key.get_pressed()
        
    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)

    for enemy in enemies:
        enemy[1]=enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])
    
    if pressed_keys[K_DOWN]:
        ball_rect= ball_rect.move(0, ball_speed)

    if pressed_keys[K_UP]:
        ball_rect= ball_rect.move(0, -ball_speed)

    if pressed_keys[K_RIGHT]:
        ball_rect= ball_rect.move(ball_speed, 0)
    
    if pressed_keys[K_LEFT]:
        ball_rect= ball_rect.move( -ball_speed, 0)

   

    pygame.display.flip()