import pygame
BLACK = (0,0,0)
class spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite#


    def animate(self):
        frame_4 = self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height)
        screen.blit(frame_4)
        