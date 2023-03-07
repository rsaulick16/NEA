import pygame
from spritesheet import *
import time


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
global x
global y
global k
k = 0
x = 0 
y = 690


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
my_spritesheet = Spritesheet('monkey2.png')
monkey_d1 = my_spritesheet.get_sprite(0,0,35,50)
monkey_d2 = my_spritesheet.get_sprite(100,0,35,50)
monkey_l1 = my_spritesheet.get_sprite(0,65,35,50)
monkey_l2 = my_spritesheet.get_sprite(100,65,35,50)
monkey_r1 = my_spritesheet.get_sprite(0,110,45,50)
monkey_r2 = my_spritesheet.get_sprite(100,110,45,50)
monkey_u1 = my_spritesheet.get_sprite(0,160,35,40)
monkey_u2 = my_spritesheet.get_sprite(100,160,35,40)
#monkey_d1 = pygame.transform.scale(monkey_d1, (50,70))
#monkey_d2 = pygame.transform.scale(monkey_d2, (50,70))
BG = (50, 50, 50)
BLACK = (0, 0, 0)
diamond = ((16, 16), (7, 7),
    (0, 0, 1, 0, 3, 128, 7, 192, 14, 224, 28, 112, 56, 56, 112, 28, 56,
     56, 28, 112, 14, 224, 7, 192, 3, 128, 1, 0, 0, 0, 0, 0),
    (1, 0, 3, 128, 7, 192, 15, 224, 31, 240, 62, 248, 124, 124, 248, 62,
     124, 124, 62, 248, 31, 240, 15, 224, 7, 192, 3, 128, 1, 0, 0, 0))
arrow = ((16, 16), (0, 0),
    (0x00,0x00,0x40,0x00,0x60,0x00,0x70,0x00,0x78,0x00,0x7C,0x00,0x7E,0x00,0x7F,0x00,
     0x7F,0x80,0x7C,0x00,0x6C,0x00,0x46,0x00,0x06,0x00,0x03,0x00,0x03,0x00,0x00,0x00),
    (0x40,0x00,0xE0,0x00,0xF0,0x00,0xF8,0x00,0xFC,0x00,0xFE,0x00,0xFF,0x00,0xFF,0x80,
     0xFF,0xC0,0xFF,0x80,0xFE,0x00,0xEF,0x00,0x4F,0x00,0x07,0x80,0x07,0x80,0x03,0x00))




start_img = pygame.image.load('game.jpg')
def updateX(cap, direction):
    k = 0
    if direction == 0:
        while x <= cap:
            x = x + 10
            if k == 0:
                screen.blit(frame_0, (y, x))
                pygame.display.update()
                k = 1
            else:
                screen.blit(frame_1, (y, x))
                pygame.display.update()
                k = 0
    if direction == 1:
        while x >= cap:
            x = x - 10
            if k == 0:
                screen.blit(frame_0, (y, x))
                pygame.display.update()
                k = 1
            else:
                screen.blit(frame_1, (y, x))
                pygame.display.update()
                k = 0

    
def updateY(cap, direction):
    j = 0
    if direction == 0:
        while y <= cap:
            y = y + 10
            if j == 0:
                screen.blit(frame_0, (y, x))
                pygame.display.update()
                j = 1
            else:
                screen.blit(frame_1, (y, x))
                pygame.display.update()
                j = 0
    if direction == 1:
        while y >= cap:
            y = y - 10
            if j == 0:
                screen.blit(frame_0, (y, x))
                pygame.display.update()
                j = 1
            else:
                screen.blit(frame_1, (y, x))
                pygame.display.update()
                j = 0

def spawnEnemy():
    interval = 0.01
    x = 0
    y = 690
    k = 0
    while x <= 140:
        x = x + 10
        if k == 0:
            screen.blit(monkey_d1, (690, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_d2, (690, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while y >= 580:
        y = y - 10
        if k == 0:
            screen.blit(monkey_l1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_l2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while x >= 90:
        x = x - 10
        if k == 0:
            screen.blit(monkey_u1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_u2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while y >= 80:
        y = y - 10
        if k == 0:
            screen.blit(monkey_l1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_l2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while x <= 270:
        x = x + 10
        if k == 0:
            screen.blit(monkey_d1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_d2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
        print(y)
    while y <= 170:
        y = y + 10
        if k == 0:
            screen.blit(monkey_r1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_r2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while x >= 200:
        x = x - 10
        if k == 0:
            screen.blit(monkey_u1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_u2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while y <= 260:
        y = y + 10
        if k == 0:
            screen.blit(monkey_r1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_r2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while x <= 270:
        x = x + 10
        if k == 0:
            screen.blit(monkey_d1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_d2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while y <= 360:
        y = y + 10
        if k == 0:
            screen.blit(monkey_r1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_r2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while x >= 200:
        x = x - 10
        if k == 0:
            screen.blit(monkey_u1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_u2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while y <= 460:
        y = y + 10
        if k == 0:
            screen.blit(monkey_r1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_r2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while x <= 350:
        x = x + 10
        if k == 0:
            screen.blit(monkey_d1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_d2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while y <= 580:
        y = y + 10
        if k == 0:
            screen.blit(monkey_r1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_r2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while x >= 260:
        x = x - 10
        if k == 0:
            screen.blit(monkey_u1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_u2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while y <= 690:
        y = y + 10
        if k == 0:
            screen.blit(monkey_r1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_r2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while x <= 450:
        x = x + 10
        if k == 0:
            screen.blit(monkey_d1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_d2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while y >= 350:
        y = y - 10
        if k == 0:
            screen.blit(monkey_l1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_l2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while x >= 380:
        x = x - 10
        if k == 0:
            screen.blit(monkey_u1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_u2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(interval)
        screen.blit(start_img,(0,0))
    while y >= 1:
        y = y - 10
        if k == 0:
            screen.blit(monkey_l1, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(monkey_l2, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(0.1)
        screen.blit(start_img,(0,0))
#need to add a spawnEnenmy class
        
    

run = True
x = 0
k= 0
while run:
    a = pygame.mouse.get_pos()
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    screen.blit(start_img,(0,0))      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #screen.blit(monkey_d1, (100,0))
    #screen.blit(monkey_d2, (0,0))
    #screen.blit(monkey_l1, (0,0))
    #screen.blit(monkey_l2, (0,0))
    #screen.blit(monkey_r1, (0,0))
    #screen.blit(monkey_r2, (0,0))
    #screen.blit(monkey_u1, (0,0))
    #screen.blit(monkey_u2, (0,0))
    spawnEnemy()


    pygame.display.update()

pygame.quit()
