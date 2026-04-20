import pygame 
import sys 
from pygame_func import draw_background, draw_sweep, inches_to_px, plot_object
import pandas as pd 
import threading
from read_data import read_data

pygame.init()

# initialize screen display 
WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar System")
clock = pygame.time.Clock()

running = True

data_lock = threading.Lock()
shared_state = {"angle": 0, "points": []}

# start read_data thread 
threading.Thread(target=read_data, args=(data_lock, shared_state), daemon=True).start()

#start game loop running
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
            sys.exit()
        
    with data_lock:
        angle = shared_state["angle"]
        points = shared_state["points"].copy()
        
    screen.fill("black")    
    draw_background(screen, CENTER)
    draw_sweep(screen, CENTER, angle)
    
    try:
        for point in points:
            point_angle = point["position"]
            point_distance = inches_to_px(point["distance"])
            if point_distance <= 500:
                plot_object(screen, CENTER, point_distance, point_angle)
    except Exception as e:
        print(f"error: {type(e).__name__}")


    
    pygame.display.flip()
    clock.tick(60)