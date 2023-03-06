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
