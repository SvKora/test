import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
from os import listdir

pygame.init()
FPS =pygame.time.Clock()

screen = width, heigth =800, 600
font=pygame.font.SysFont('Verdana', 20)

BLACK=0, 0, 0
WHITE=255, 255, 255
BLUE= 128,166, 255
YELLOW=255, 255, 0
RED=255, 0, 0
main_surface = pygame.display.set_mode(screen)

IMG_PATH='goose'
#ball = pygame.Surface((20, 20))
#ball.fill(YELLOW)
ball_imgs=[pygame.image.load(IMG_PATH + '/' + file).convert_alpha() for file in listdir(IMG_PATH)]
ball= ball_imgs[0]
ball_rect=ball.get_rect()
ball_speed = 5

def create_enemy():
    #enemy = pygame.Surface((30, 30))
    #enemy.fill(RED)
    enemy= pygame.image.load('enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(width, random.randint(0, heigth), *enemy.get_size())
    enemy_speed=random.randint(1, 5)
    return [enemy, enemy_rect, enemy_speed]

CHANGE_IMG =pygame.USEREVENT+3
pygame.time.set_timer(CHANGE_IMG, 125)

CREATE_ENEMY =pygame.USEREVENT+1
pygame.time.set_timer(CREATE_ENEMY, 2500)

enemies =[]


def create_bonus():
    #bonus = pygame.Surface((10, 10))
    #bonus.fill(WHITE)
    bonus= pygame.image.load('bonus.png').convert_alpha()
    bonus_rect = pygame.Rect(random.randint(100, width-100), 0, *bonus.get_size())
    bonus_speed=-random.randint(1, 5)
    return [bonus, bonus_rect, bonus_speed]

bg =pygame.transform.scale( pygame.image.load('background.png').convert(), screen)
bgx=0
bgx2=bg.get_width()
bg_speed=3

CREATE_BONUS =pygame.USEREVENT+2
pygame.time.set_timer(CREATE_BONUS, 1500)

img_index=0
scores = 0

bonuses=[]


is_working = True

while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
           is_working = False

        if event.type == CREATE_ENEMY:
           enemies.append(create_enemy())
        
        if event.type == CREATE_BONUS:
           bonuses.append(create_bonus())

        if event.type==CHANGE_IMG:
           img_index+=1
           if img_index == len(ball_imgs):
              img_index=0
           ball = ball_imgs[img_index]
            
    

    pressed_keys = pygame.key.get_pressed()
        
    #main_surface.fill(BLACK)
  
    #main_surface.blit(bg, (0, 0))

    bgx-=bg_speed
    bgx2-=bg_speed

    if bgx < -bg.get_width():
        bgx=bg.get_width()

    if bgx2 < -bg.get_width():
        bgx2=bg.get_width()

    
    main_surface.blit(bg, (bgx, 0))
    main_surface.blit(bg, (bgx2, 0))

    main_surface.blit(ball, ball_rect)
    main_surface.blit(font.render(str(scores), True, BLUE), (width-30, 0))

    for enemy in enemies:
        enemy[1]=enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        
        if ball_rect.colliderect(enemy[1]):
            is_working= False


    for bonus in bonuses:
        bonus[1]=bonus[1].move(0, -bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom >= heigth:
            bonuses.pop(bonuses.index(bonus))

        if ball_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores +=1
        

    if pressed_keys[K_DOWN] and not ball_rect.bottom>=heigth:
        ball_rect= ball_rect.move(0, ball_speed)

    if pressed_keys[K_UP] and not ball_rect.top<=0:
        ball_rect= ball_rect.move(0, -ball_speed)

    if pressed_keys[K_RIGHT] and not ball_rect.right>=width:
        ball_rect= ball_rect.move(ball_speed, 0)
    
    if pressed_keys[K_LEFT] and not ball_rect.left<=0:
        ball_rect= ball_rect.move( -ball_speed, 0)
    
   
  

    pygame.display.flip()