# floorfurniture.py
import pygame

from src.objects.furniture.furniture import Furniture
from src.data.furniture_registry import FurnitureRegistry
from src.objects.room.room_config import RoomConfig

from dataclasses import dataclass, field

from src.utils.iso_utils import IsoUtils


@dataclass
class FloorFurniture:
    roomX: int
    roomY: int
    roomZ: int
    direction: int
    type: str

    __furniture_data: Furniture = field(init=False, repr=False)
    __screen_x: int = field(init=False)
    __screen_y: int = field(init=False)

    def __post_init__(self):

        self.__furniture_data = FurnitureRegistry.load_furniture(self.type)
        
        if not self.__furniture_data:
            raise ValueError(f"Can't load Furniture-Type: '{self.type}' ")

        iso_x, iso_y = IsoUtils.grid_to_iso(self.roomX, self.roomY)

        self.__screen_x = iso_x + RoomConfig.OFFSET_X
        self.__screen_y = iso_y + RoomConfig.OFFSET_Y

        print(self.__furniture_data)


