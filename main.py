import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                import snake
            if event.key == pygame.K_BACKSPACE:
                import runner_video


        
    screen.fill((0,212,53))
    pygame.display.update()
