# floorfurniture.py
import pygame

from src.objects.room import room_config
import src.objects.room.room as room

from dataclasses import dataclass, field

from src.utils.iso_utils import IsoUtils


@dataclass
class FloorFurniture:
    roomX: int
    roomY: int
    roomZ: int
    direction: int
    type: str

    __screen_x: int = field(init=False)
    __screen_y: int = field(init=False)

    def __post_init__(self):

        iso_x, iso_y = IsoUtils.grid_to_iso(self.roomX, self.roomY)

        self.__screen_x = iso_x + room_config.OFFSET_X
        self.__screen_y = iso_y + room_config.OFFSET_Y


