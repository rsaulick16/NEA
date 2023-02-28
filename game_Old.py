import pygame
from spritesheet import *
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('monkey2.bmp').convert_alpha()
#sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)


#frame_0 = sprite_sheet.get_image(0, 50, 50, 1, BLACK)
#frame_1 = sprite_sheet.get_image(25, 50, 50, 1, BLACK)
#frame_2 = sprite_sheet.get_image(0, 100, 100, 2, BLACK)
#frame_3 = sprite_sheet.get_image(10, 24, 24, 3, BLACK)

start_img = pygame.image.load('game.jpg')

run = True
x = 0
k = 0
enemy = True
"""
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
"""        
    
while run:
    screen.blit(start_img,(0,0))
    #time.sleep(10)
    #screen.blit(frame_1, (0, 400))
	#screen.blit(frame_2, (150, 0))
	#screen.blit(frame_3, (250, 0))
    #event handler
    spritesheet.animate()
    if enemy == True:
        pass
        #spawnEnemy()
        #enemy = False
   
        
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
         run = False

    pygame.display.update()

pygame.quit()
   
