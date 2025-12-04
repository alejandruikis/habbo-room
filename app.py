import os
from src.objects.furniture.floorfurniture import FloorFurniture
from src.data.furniture_registry import FurnitureRegistry
import definitions
import pygame
from src.objects.room.room import Room


# Init
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

FurnitureRegistry.preload_all(["club_sofa"])

room = Room(screen)

club_sofa = FloorFurniture(
    roomX=0,
    roomY=0,
    roomZ=0,
    direction=2,
    type="club_sofa"
)

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