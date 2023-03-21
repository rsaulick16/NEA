import pygame
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
start_img = pygame.image.load('game.jpg')
class Enemy:
    def __init__(self):
        self.speed = 0
        self.health = 0
        self.number = 0
        self.path_points = [(720, 6), (712,181), (585, 170), (580, 104), (92, 102), (95,303), (191,293), (196,221), (293,216), (292,300), (390,303), (400,211), (488,218), (500,396), (610,401), (603,282), (723,284), (720,473), (375,476), (370,402), (2,403)]
        self.sprite_pos = pygame.math.Vector2(self.path_points[0])
        self.target_point_index = 1
        self.target_point = pygame.math.Vector2(self.path_points[self.target_point_index])
        self.sprite_speed = 1
    
    def spawnSprite(self, sprite):
        if (self.target_point - self.sprite_pos).length() < self.sprite_speed:
            self.target_point_index += 1   
            print("1")
            if self.target_point_index == 20:
                print("score:999")
            self.target_point = pygame.math.Vector2(self.path_points[self.target_point_index])
            print("2")
        screen.blit(sprite, (self.sprite_pos.x, self.sprite_pos.y))
        pygame.display.flip()
        print("3")

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
    
