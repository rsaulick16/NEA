import pygame
import time
import random
from spritesheet import *
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
start_img = pygame.image.load('game.jpg')
my_spritesheet = Spritesheet('monkey2.png')


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        monkey_d1 = my_spritesheet.get_sprite(0,0,35,50)
        self.alive = 1
        self.speed = 0
        self.health = 2
        self.number = 0
        self.path_points = [(720, 6), (712,181), (585, 170), (580, 104), (92, 102), (95,303), (191,293), (196,221), (293,216), (292,300), (390,303), (400,211), (488,218), (500,396), (610,401), (603,282), (723,284), (720,473), (375,476), (370,402), (2,403)]
        self.sprite_pos = pygame.math.Vector2(self.path_points[0])
        self.sprite_pos.x = 720
        self.sprite_pos.y = 6
        self.target_point_index = 1
        self.target_point = pygame.math.Vector2(self.path_points[self.target_point_index])
        self.sprite_speed = 1
        self.j = 0
        self.hitbox = self.hitbox = pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.sprite_pos.x, self.sprite_pos.y, 20, 60),  2)
        #pygame.sprite.Sprite.__init__(self)
        self.image = monkey_d1
        #self.rect = self.image.get_rect()
        
    
    def spawnSprite(self):
        #self.player_group = pygame.sprite.Group()
        #self.player_group.add(self.image)
        if self.j == 0: 
            direction = self.target_point - self.sprite_pos
            direction.normalize_ip()
            self.sprite_pos += direction * self.sprite_speed
            print("j is",self.j)
            if (self.target_point - self.sprite_pos).length() < self.sprite_speed:
                self.target_point_index += 1   
                print("1")
                if self.target_point_index < 21:
                    self.target_point = pygame.math.Vector2(self.path_points[self.target_point_index])
                else:
                    print("lose")
                    self.j = 10
                print("2")
            screen.blit(self.image, (self.sprite_pos.x, self.sprite_pos.y))
            pygame.display.flip()
            print("3")
            if self.target_point_index == 20 :
                #self.target_point_index + 1
                print("?")
    def setHitbox(self):       
        self.hitbox = pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.sprite_pos.x, self.sprite_pos.y, 35, 60),  2)
    def testFunction(self):
        print("!!!!!")
    def getHitbox(self,event):
        run = 1
        if run == 1:
            if self.hitbox.collidepoint(event.pos):
                self.health = self.health - 1
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", self.health)
            
            if self.health <= 0:
                    print("ASDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
                    self.hitbox.move(100,100)
                    self.j = 1
                    run = run - 1
                                
    def moveEnemy(self,D1,D2,L1,L2,U1,U2,R1,R2):
        interval = 0.1
        k = 0
        u = 0
        if self.p >= 0:
            while self.x <= 140:
                self.x = self.x + 10
                if k == 0:
                    screen.blit(D1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(D2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            print(u)
            u+1
            while self.y >= 580:
                self.y = self.y - 10
                if k == 0:
                    screen.blit(L1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(L2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            print(u)
            u+1
            self.moveEnemy(D1,D2,L1,L2,U1,U2,R1,R2)
            while self.x >= 90:
                self.x = self.x - 10
                if k == 0:
                    screen.blit(U1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(U2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            print(u)
            u+1
            while self.y >= 80:
                self.y = self.y - 10
                if k == 0:
                    screen.blit(L1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(L2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.x <= 270:
                self.x = self.x + 10
                if k == 0:
                    screen.blit(D1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(D2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.y <= 170:
                self.y = self.y + 10
                if k == 0:
                    screen.blit(R1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(R2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.x >= 200:
                self.x = self.x - 10
                if k == 0:
                    screen.blit(U1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(U2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.y <= 260:
                self.y = self.y + 10
                if k == 0:
                    screen.blit(R1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(R2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.x <= 270:
                self.x = self.x + 10
                if k == 0:
                    screen.blit(D1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(D2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.y <= 360:
                self.y = self.y + 10
                if k == 0:
                    screen.blit(R1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(R2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.x >= 200:
                self.x = self.x - 10
                if k == 0:
                    screen.blit(U1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(U2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.y <= 460:
                self.y = self.y + 10
                if k == 0:
                    screen.blit(R1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(R2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.x <= 350:
                self.x = self.x + 10
                if k == 0:
                    screen.blit(D1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(D2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.y <= 580:
                self.y = self.y + 10
                if k == 0:
                    screen.blit(R1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(R2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.x >= 260:
                self.x = self.x - 10
                if k == 0:
                    screen.blit(U1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(U2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.y <= 690:
                self.y = self.y + 10
                if k == 0:
                    screen.blit(R1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(R2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.x <= 450:
                self.x = self.x + 10
                if k == 0:
                    screen.blit(D1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(D2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.y >= 350:
                self.y = self.y - 10
                if k == 0:
                    screen.blit(L1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(L2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.x >= 380:
                self.x = self.x - 10
                if k == 0:
                    screen.blit(U1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(U2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(interval)
                screen.blit(start_img,(0,0))
            while self.y >= 1:
                self.y = self.y - 10
                if k == 0:
                    screen.blit(L1, (self.y, self.x))
                    pygame.display.update()
                    k = 1
                else:
                    screen.blit(L2, (self.y, self.x))
                    pygame.display.update()
                    k = 0
                time.sleep(0.1)
                screen.blit(start_img,(0,0))
            self.p = self.p - 1
            print("hello")
            print(self.p)
            return
        elif self.p == -1:
            print("no")
            return   
    
