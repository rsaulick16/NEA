import pygame
from spritesheet import *
import time
from enemy import *


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Movement stuff 
#path_points = [(720, 6), (712,181), (585, 170), (580, 104), (92, 102), (95,303), (191,293), (196,221), (293,216), (292,300), (390,303), (400,211), (488,218), (500,396), (610,401), (603,282), (723,284), (720,473), (375,476), (370,402), (2,403)]
#sprite_pos = pygame.math.Vector2(path_points[0])
#target_point_index = 1
#target_point = pygame.math.Vector2(path_points[target_point_index])
#sprite_speed = 1
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
run = True
x = 1
monkey = Enemy()
while run:
    a = pygame.mouse.get_pos()
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    screen.blit(start_img,(0,0))      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    monkey.spawnSprite(monkey_d1)
           
    #direction = target_point - self.sprite_pos
    #direction.normalize_ip()
    #self.sprite_pos += direction * self.sprite_speed

    # Check if the sprite has reached the target point

            


    # Draw the sprite on the screen
    #screen.fill((255, 255, 255))  # white color
    
    #screen.blit(monkey_d1, (sprite_pos.x, sprite_pos.y))

    
        
    
    #pygame.display.flip()
    #if pygame.sprite.spritecollideany(player, enemies)
    #pygame.draw.rect(win, (255,0,0), self.hitbox,2)           

    
    #screen.blit(monkey_d1, (100,0))
    #screen.blit(monkey_d2, (0,0))
    #screen.blit(monkey_l1, (0,0))
    #screen.blit(monkey_l2, (0,0))
    #screen.blit(monkey_r1, (0,0))
    #screen.blit(monkey_r2, (0,0))
    #screen.blit(monkey_u1, (0,0))
    #screen.blit(monkey_u2, (0,0))
    #monkey = Enemy()
    #while x >= 0:
        #normal monkey
     #   x = x-1
     #   monkey.moveEnemy(monkey_d1,monkey_d2,monkey_l1,monkey_l2,monkey_u1,monkey_u2,monkey_r1,monkey_r2)
    #    print(x)
    #pygame.display.update()

pygame.quit()
