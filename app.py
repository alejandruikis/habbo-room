import os
import definitions
import pygame
from src.objects.room.room import Room


# Init
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

room = Room(screen);

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    # ...
    
    # Render
    screen.fill((0, 0, 0))
    room.render()
    pygame.display.flip()
    clock.tick(60)