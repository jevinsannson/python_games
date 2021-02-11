import pygame

pygame.init() #initialize all imported pygame modules
pygame.display.set_caption('Jevins') # Caption for the window
window_surface = pygame.display.set_mode((500, 600)) # Window size
window_surface.fill(pygame.Color('red')) # Background colour of the window

black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey = pygame.Color(128, 128, 128)   # Grey
red = pygame.Color(255, 0, 0)       # Red
green = pygame.Color(0, 255, 0)       # greeen
blue = pygame.Color(0, 0, 255)       # Blue


pygame.draw.line(window_surface, blue, (150,130), (130,170))
pygame.draw.line(window_surface, blue, (150,130), (170,170))
pygame.draw.line(window_surface, green, (130,170), (170,170))
pygame.draw.circle(window_surface, black, (100,50), 30)
pygame.draw.circle(window_surface, black, (200,50), 30)
pygame.draw.rect(window_surface, red, (100, 200, 100, 50), 2)
pygame.draw.rect(window_surface, black, (110, 260, 80, 5))

while True:
 pygame.display.update()
 for event in pygame.event.get(): # Close window on clicking close button
     if event.type == pygame.QUIT:
         pygame.quit()