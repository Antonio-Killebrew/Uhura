import os
import pygame
from sys import exit

GAME_WIDTH = 512
GAME_HEIGHT = 512

PLAYER_X = GAME_WIDTH/2
PLAYER_Y = GAME_WIDTH/2
PLAYER_WIDTH = 42
PLAYER_HEIGHT = 48

background_image = pygame.image.load(os.path.join("images","background.png"))
player_image_right = pygame.image.load(os.path.join("images","megaman-right.png"))
player_image_right = pygame.transform.scale(player_image_right,(PLAYER_WIDTH,PLAYER_HEIGHT))

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("Uhura")
clock = pygame.time.Clock()

class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_image_right

player = Player()

def draw():
    window.fill((20,18,167))
    window.blit(background_image,(0,80))
    window.blit(player.image,player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += 5
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 5

    draw()
    pygame.display.update()
    clock.tick(60)
