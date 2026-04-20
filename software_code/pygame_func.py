import pygame 
import math
import pandas as pd 
import threading 
from read_data import read_data

def draw_background(screen, CENTER):
    max_radius = 500
    for r in range(50, max_radius+1, 50):
        pygame.draw.circle(screen, (0, 100, 0), CENTER, r, 1) 
        
def draw_sweep(screen, CENTER, angle):
    length = 500
    start_pos = CENTER
    x = math.cos(math.radians(angle)) * length
    y = math.sin(math.radians(angle)) * length
    end_pos = (start_pos[0] + x, start_pos[1] - y)
    pygame.draw.line(screen, (0, 255, 0), start_pos, end_pos, width=5)
    
def inches_to_px(distance):
   return distance*100

def plot_object(screen, CENTER, point_distance, point_angle):
    x = CENTER[0] + int(point_distance * math.cos(math.radians(point_angle)))
    y = CENTER[1] - int(point_distance * math.sin(math.radians(point_angle)))
    pygame.draw.circle(screen, "red", (x, y), 5)

    