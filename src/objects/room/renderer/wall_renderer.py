import pygame
from src.objects.room.room_config import RoomConfig, TileType

class WallRenderer:
    
    @staticmethod
    def draw_left_wall(surface: pygame.Surface, x: int, y: int):
        wall_height = RoomConfig.TILE_HEIGHT * RoomConfig.WALL_HEIGHT_MULTIPLIER
        
        # Main Wall
        main_points = [
            (x, y),
            (x - RoomConfig.TILE_WIDTH // 2, y + RoomConfig.TILE_HEIGHT // 2),
            (x - RoomConfig.TILE_WIDTH // 2, y + RoomConfig.TILE_HEIGHT // 2 + wall_height),
            (x, y + wall_height)
        ]
        
        bx = x - RoomConfig.WALL_THICKNESS
        by = y - RoomConfig.WALL_THICKNESS
        
        top_points = [
            (bx, by),
            (bx - RoomConfig.TILE_WIDTH // 2, by + RoomConfig.TILE_HEIGHT // 2),
            (bx - RoomConfig.TILE_WIDTH // 2 + RoomConfig.WALL_THICKNESS, 
             by + RoomConfig.TILE_HEIGHT // 2 + RoomConfig.WALL_THICKNESS),
            (bx + RoomConfig.WALL_THICKNESS, by + RoomConfig.WALL_THICKNESS)
        ]
        
        left_side_points = [
            (bx - RoomConfig.TILE_WIDTH // 2, by + RoomConfig.TILE_HEIGHT // 2),
            (bx - RoomConfig.TILE_WIDTH // 2 + RoomConfig.WALL_SIDE_THICKNESS, 
             by + RoomConfig.TILE_HEIGHT // 2),
            (bx - RoomConfig.TILE_WIDTH // 2 + RoomConfig.WALL_SIDE_THICKNESS, 
             by + RoomConfig.TILE_HEIGHT // 2 + wall_height + 10),
            (bx - RoomConfig.TILE_WIDTH // 2, 
             by + RoomConfig.TILE_HEIGHT // 2 + wall_height + 6.5)
        ]
        
        pygame.draw.polygon(surface, RoomConfig.WALL_SIDE_LEFT_COLOR, left_side_points)
        pygame.draw.polygon(surface, RoomConfig.WALL_TOP_BORDER_COLOR, top_points)
        pygame.draw.polygon(surface, RoomConfig.WALL_LEFT_COLOR, main_points)
    
    @staticmethod
    def draw_top_wall(surface: pygame.Surface, x: int, y: int):
        wall_height = RoomConfig.TILE_HEIGHT * RoomConfig.WALL_HEIGHT_MULTIPLIER
        
        main_points = [
            (x, y),
            (x + RoomConfig.TILE_WIDTH // 2, y + RoomConfig.TILE_HEIGHT // 2),
            (x + RoomConfig.TILE_WIDTH // 2, y + RoomConfig.TILE_HEIGHT // 2 + wall_height),
            (x, y + wall_height)
        ]
        
        bx = x + RoomConfig.WALL_THICKNESS
        by = y - RoomConfig.WALL_THICKNESS
        
        top_points = [
            (bx, by),
            (bx + RoomConfig.TILE_WIDTH // 2, by + RoomConfig.TILE_HEIGHT // 2),
            (bx + RoomConfig.TILE_WIDTH // 2 - RoomConfig.WALL_THICKNESS, 
             by + RoomConfig.TILE_HEIGHT // 2 + RoomConfig.WALL_THICKNESS),
            (bx - RoomConfig.WALL_THICKNESS, by + RoomConfig.WALL_THICKNESS)
        ]
        
        right_side_points = [
            (bx + RoomConfig.TILE_WIDTH // 2, by + RoomConfig.TILE_HEIGHT // 2),
            (bx + RoomConfig.TILE_WIDTH // 2 - RoomConfig.WALL_SIDE_THICKNESS, 
             by + RoomConfig.TILE_HEIGHT // 2),
            (bx + RoomConfig.TILE_WIDTH // 2 - RoomConfig.WALL_SIDE_THICKNESS, 
             by + RoomConfig.TILE_HEIGHT // 2 + wall_height + 10),
            (bx + RoomConfig.TILE_WIDTH // 2, 
             by + RoomConfig.TILE_HEIGHT // 2 + wall_height + 6.5)
        ]
        
        pygame.draw.polygon(surface, RoomConfig.WALL_SIDE_RIGHT_COLOR, right_side_points)
        pygame.draw.polygon(surface, RoomConfig.WALL_TOP_BORDER_COLOR, top_points)
        pygame.draw.polygon(surface, RoomConfig.WALL_TOP_COLOR, main_points)
        pygame.draw.polygon(surface, RoomConfig.WALL_TOP_COLOR, main_points, 2)