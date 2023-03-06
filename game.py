import pygame
import spritesheet
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
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('monkey2.bmp').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

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



frame_0 = sprite_sheet.get_image(0, 50, 50, 1, BLACK)
frame_1 = sprite_sheet.get_image(2, 50, 50, 1, BLACK)
frame_2 = sprite_sheet.get_image(2, 24, 24, 3, BLACK)
frame_3 = sprite_sheet.get_image(3, 24, 24, 3, BLACK)
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

    
def updateX(cap, direction):
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
    x = 0
    y = 690
    k = 0
    while x <= 140:
        x = x + 10
        if k == 0:
            screen.blit(frame_0, (690, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(frame_1, (690, x))
            pygame.display.update()
            k = 0
        time.sleep(0.1)
        screen.blit(start_img,(0,0))
       # print(x)
    while y >= 580:
        y = y - 10
        if k == 0:
            screen.blit(frame_0, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(frame_1, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(0.1)
        screen.blit(start_img,(0,0))
    while x >= 90:
        x = x - 10
        if k == 0:
            screen.blit(frame_0, (y, x))
            pygame.display.update()
            k = 1
        else:
            screen.blit(frame_1, (y, x))
            pygame.display.update()
            k = 0
        time.sleep(0.1)
        screen.blit(start_img,(0,0))
       # print(x)
        
    

run = True
x = 0
k= 0
while run:
    a = pygame.mouse.get_pos()
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    screen.blit(start_img,(0,0))
    #time.sleep(10)
    #screen.blit(frame_1, (0, 400))
	#screen.blit(frame_2, (150, 0))
	#screen.blit(frame_3, (250, 0))
    #event handler
    print(a)

    



        
    for event in pygame.event.get():
        if k <= 10:
            spawnEnemy()
            k = k+1

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
   

        elif event.type == pygame.MOUSEBUTTONDOWN:
            spawnEnemy()
            
         
         





    pygame.display.update()

pygame.quit()
