import pygame
from src.objects.room.room_config import RoomConfig, TileType
from src.utils.iso_utils import IsoUtils
from src.objects.room.renderer.tile_renderer import TileRenderer
from src.objects.room.renderer.wall_renderer import WallRenderer


class Room:
    def __init__(self, surface: pygame.Surface, tilemap: str = ""):
        self.surface = surface
        self.tilemap = tilemap if tilemap != "" else self._default_tilemap()
        self.tiles = self._parse_tilemap()
    
    def _default_tilemap(self) -> str:
        return ("xxxxx\n"
                "xoooo\n"
                "xoooo\n"
                "xoooo\n"
                "xoooo")
    
    def _parse_tilemap(self) -> list[list[int]]:
        def char_to_tile(ch: str) -> int:
            return TileType.WALL if ch == "x" else TileType.FLOOR if ch == "o" else None
        
        lines = [line.strip() for line in self.tilemap.split("\n") if line.strip()]
        return [[char_to_tile(ch) for ch in row] for row in lines]
    
    def render(self):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                screen_x, screen_y = IsoUtils.grid_to_screen(x, y)
                
                if tile == TileType.WALL:
                    self._render_wall(x, y, row, screen_x, screen_y)
                elif tile == TileType.FLOOR:
                    self._render_floor(x, y, row, screen_x, screen_y)
    
    def _render_wall(self, grid_x: int, grid_y: int, row: list, screen_x: int, screen_y: int):

        # check if right is floor -> draw left wall
        if grid_x + 1 < len(row) and row[grid_x + 1] == TileType.FLOOR:
            wall_x = screen_x + RoomConfig.TILE_WIDTH // 2
            wall_y = screen_y - RoomConfig.TILE_HEIGHT - (RoomConfig.TILE_HEIGHT // 2)
            WallRenderer.draw_left_wall(self.surface, wall_x, wall_y)
        
        # check if below is floor -> draw top wall
        if grid_y + 1 < len(self.tiles) and self.tiles[grid_y + 1][grid_x] == TileType.FLOOR:
            wall_x = screen_x - RoomConfig.TILE_WIDTH // 2
            wall_y = screen_y - RoomConfig.TILE_HEIGHT - (RoomConfig.TILE_HEIGHT // 2)
            WallRenderer.draw_top_wall(self.surface, wall_x, wall_y)
    
    def _render_floor(self, grid_x: int, grid_y: int, row: list, screen_x: int, screen_y: int):

        TileRenderer.draw(self.surface, screen_x, screen_y)
        
        # draw outlines
        if grid_y + 1 == len(self.tiles):
            TileRenderer.draw_left_outline(self.surface, screen_x, screen_y)
        
        if grid_x + 1 == len(row):
            TileRenderer.draw_right_outline(self.surface, screen_x, screen_y)
