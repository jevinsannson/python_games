import pygame
import random
import math
print('hello')
# Initialize  pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load("images/background.png")

# Title and icon
pygame.display.set_caption("Cybersquare - Space invaders")
icon = pygame.image.load("images/cs_logo.png")
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    # background
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
           