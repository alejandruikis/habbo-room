import pygame

from src.objects.furniture.furniture import Furniture
from src.data.furniture_registry import FurnitureRegistry
from src.objects.room.room_config import RoomConfig

from dataclasses import dataclass, field

from src.utils.iso_utils import IsoUtils


@dataclass
class FloorFurniture:
    room_x: int
    room_y: int
    room_z: int
    direction: int
    type: str

    __furniture_data: Furniture = field(init=False, repr=False)

    def __post_init__(self):

        self.__furniture_data = FurnitureRegistry.load_furniture(self.type)
        
        if not self.__furniture_data:
            raise ValueError(f"Can't load Furniture-Type: '{self.type}' ")

    
    def render(self, surface: pygame.Surface):
        drawn_assets = set()
        
        for tile_x in range(self.__furniture_data.tile_width):
            for tile_y in range(self.__furniture_data.tile_height):
   
                abs_grid_x = self.room_x + tile_x
                abs_grid_y = self.room_y + tile_y
                
                screen_x, screen_y = IsoUtils.grid_to_screen(abs_grid_x, abs_grid_y)
                
                for layer in self.__furniture_data.layers:
                    asset = layer.assets.get(self.direction)
                    
                    if asset:
                        asset_key = getattr(asset, "name", None) or id(asset)
                        if asset_key in drawn_assets:
                            continue
                        
                        sprite = asset.get_sprite(self.__furniture_data.all_assets)
                        
                        if sprite:
                            render_x = screen_x - asset.offset_x
                            render_y = screen_y - asset.offset_y
                            surface.blit(sprite, (render_x, render_y))
                            drawn_assets.add(asset_key)