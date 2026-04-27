import pygame
from sys import exit

GAME_WIDTH = 512
GAME_HEIGHT = 512

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("Uhura")
clock = pygame.time.Clock()

def draw():
    window.fill((20,18,167))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    draw()
    pygame.display.update()
    clock.tick(60)
