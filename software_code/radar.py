import pygame 
import sys 
from pygame_func import draw_background, draw_sweep

pygame.init()

# initialize screen display 
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar System")
clock = pygame.time.Clock()

angle = 0
direction = "clockwise"
running = True

#start game loop running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
            sys.exit()
        
    screen.fill("black")    
    draw_background(screen, WIDTH, HEIGHT)
    draw_sweep(screen, WIDTH, HEIGHT, angle)
    
    if angle < 180 and direction == "clockwise":
        angle += 1
        if angle == 179:
            direction = "anticlockwise"
        
    else:
        angle -= 1
        if angle == 1:
            direction = "clockwise"
    
    pygame.display.flip()
    clock.tick(60)