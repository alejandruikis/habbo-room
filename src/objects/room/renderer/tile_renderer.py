import pygame
from src.objects.room.room_config import RoomConfig, TileType

class TileRenderer:
    
    @staticmethod
    def draw(surface: pygame.Surface, x: int, y: int):
        points = [
            (x, y),
            (x + RoomConfig.TILE_WIDTH // 2, y + RoomConfig.TILE_HEIGHT // 2),
            (x, y + RoomConfig.TILE_HEIGHT),
            (x - RoomConfig.TILE_WIDTH // 2, y + RoomConfig.TILE_HEIGHT // 2)
        ]
        pygame.draw.polygon(surface, RoomConfig.FLOOR_COLOR, points)
        pygame.draw.polygon(surface, RoomConfig.FLOOR_BORDER_COLOR, points, 1)
    
    @staticmethod
    def draw_left_outline(surface: pygame.Surface, x: int, y: int):
        points = [
            (x, y),
            (x + RoomConfig.TILE_WIDTH // 2, y + RoomConfig.TILE_HEIGHT // 2),
            (x, y + RoomConfig.TILE_HEIGHT),
            (x - RoomConfig.TILE_WIDTH // 2, y + RoomConfig.TILE_HEIGHT // 2)
        ]
        bottom = points[2]
        left = points[3]
        pygame.draw.line(surface, RoomConfig.FLOOR_LEFT_OUTLINE, bottom, left, 10)
    
    @staticmethod
    def draw_right_outline(surface: pygame.Surface, x: int, y: int):
        points = [
            (x, y),
            (x + RoomConfig.TILE_WIDTH // 2, y + RoomConfig.TILE_HEIGHT // 2),
            (x, y + RoomConfig.TILE_HEIGHT),
            (x - RoomConfig.TILE_WIDTH // 2, y + RoomConfig.TILE_HEIGHT // 2)
        ]
        bottom = points[2]
        right = points[1]
        pygame.draw.line(surface, RoomConfig.FLOOR_RIGHT_OUTLINE, bottom, right, 10)

