import pygame

# Init
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


def create_room(tilemap = None):
    tile_size = 64

    if (tilemap is None):
        # x = wall
        # o = floor
        example_tilemap = ("xxxx\n"
                        "xooo\n"
                        "xooo\n"
                        "xooo")
    
    converted_tilemap = convert_tilemap(example_tilemap)
    for y, row in enumerate(converted_tilemap):
        for x, tile in enumerate(row):
            if tile == 1:
                color = (0, 0, 0)  # Wall
            elif tile == 0:
                color = (200, 200, 200)  # Floor
            else:
                continue
            
            rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, color, rect)

def convert_tilemap(tilemap):
    def to_tile_type(ch):
        # 'x' = 1 (wall), 'o' = 0 (floor)
        if ch == "x":
            return 1
        if ch == "o":
            return 0
        return None

    lines = tilemap.split("\n")
    rows = [line.strip() for line in lines]                
    rows = [r for r in rows if len(r) > 0]                  
    converted = [[to_tile_type(ch) for ch in row] for row in rows]
    return converted



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    # ...
    
    # Render
    screen.fill((255, 255, 255))
    
    create_room(None)

    pygame.display.flip()
    clock.tick(60)