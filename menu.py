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
        if count == 0:    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_img = pygame.image.load('game_menu.png')
                    count = count + 1  
        if count == 1:        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    start_img = pygame.image.load('game_title.png')
                    count = count - 1  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    start_img = pygame.image.load('game_scoreboard.png')
                    count = count + 1 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start_img = pygame.image.load('game_setup.png')
                    count = count + 5
                    print(count)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    start_img = pygame.image.load('game_instructions_temp.png')
                    count = count + 10 
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    start_img = pygame.image.load('game_instructions_temp.png')
                    runing = False
        if count == 2:            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    start_img = pygame.image.load('game_menu.png')
                    count = count - 1   
        if count == 6:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    start_img = pygame.image.load('game_menu.png')
                    count = count - 5 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start_img = pygame.image.load('game.png')
                    count = count + 10 
                    print(count)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5:
                    start_img = pygame.image.load('game.png')
                    count = count + 20 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_6:
                    start_img = pygame.image.load('game.png')
                    count = count + 30 

                    
                    
                    
                    
                    
        if count == 11:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    start_img = pygame.image.load('game_menu.png')
                    count = count - 10
                         
        if count == 16:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    start_img = pygame.image.load('game_menu.png')
                    count = count - 15
                        
        if count == 26:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    start_img = pygame.image.load('game_menu.png')
                    count = count - 25
                       
        if count == 36:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    start_img = pygame.image.load('game_menu.png')
                    count = count - 35
                                 
          
            
        pygame.display.update()         
pygame.quit()
