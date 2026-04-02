import pygame 
import math

def draw_background(screen, WIDTH, HEIGHT):
    max_radius = 500
    CENTER = (WIDTH // 2, HEIGHT)
    for r in range(50, max_radius+1, 50):
        pygame.draw.circle(screen, (0, 100, 0), CENTER, r, 1) 
        
def draw_sweep(screen, WIDTH, HEIGHT, angle):
    length = 500
    start_pos = (WIDTH // 2, HEIGHT)
    x = math.cos(math.radians(angle)) * length
    y = math.sin(math.radians(angle)) * length
    end_pos = (start_pos[0] - x, start_pos[1] - y)
    pygame.draw.line(screen, (0, 255, 0), start_pos, end_pos, width=5)