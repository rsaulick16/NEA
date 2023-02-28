import pygame
import spritesheet
import time


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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

def spawnEnemy():
    k = 0
    for i in range(0,160,10):
        x = i
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
        print(i)

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
    spawnEnemy()
    



        
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
         run = False
     elif event.type == pygame.MOUSEBUTTONDOWN:
         spawnEnemy()
        
         
         





    pygame.display.update()

pygame.quit()