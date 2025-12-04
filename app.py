import os
from src.objects.furniture import floorfurniture
from src.data.furniture_extractor import FurnitureExtractor
import definitions
import pygame
from src.objects.room.room import Room


# Init
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

FurnitureExtractor("club_sofa").extract()

room = Room(screen)

club_sofa = floorfurniture(
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