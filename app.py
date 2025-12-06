from src.objects.furniture.floorfurniture import Furniture
from src.data.furniture_registry import FurnitureRegistry
import pygame
from src.objects.room.room import Room

import pygame_gui

# Init
pygame.init()
screen = pygame.display.set_mode((800, 600))


FurnitureRegistry.preload_all(["club_sofa"])

room = Room(screen)

club_sofa = Furniture(
    room_x=2,
    room_y=3,
    room_z=0,
    direction=6,
    type="club_sofa"
)

window_surface = pygame.display.set_mode((800, 600))

manager = pygame_gui.UIManager((800, 600))
clock = pygame.time.Clock()

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Say Hello',
                                            manager=manager)

running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print("Hello World!")

    manager.update(time_delta)

    # Render
    screen.fill((0, 0, 0))
    room.render()
    club_sofa.render(screen)

    manager.draw_ui(window_surface)
    pygame.display.flip()