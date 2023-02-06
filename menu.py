import pygame
import sys
import time
from pygame.locals import *
pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width,height))
start_img = pygame.image.load('game_title.png')
runing = True
count = 0
  

 
while runing:
    window.blit(start_img,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_img = pygame.image.load('game_menu.png')
                count = count + 1  
        if count == 1:        
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                start_img = pygame.image.load('game_title.png')
                count = count - 1  
        pygame.display.update()         
pygame.quit()

