import pygame 
import sys 

pygame.init()

# initialize screen display 
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar System")

running = True

#start game loop running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
            sys.exit()
            
    screen.fill((77, 77, 51))
    pygame.display.flip()