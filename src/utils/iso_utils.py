from src.objects.room.room_config import RoomConfig

class IsoUtils:
    
    @staticmethod
    def grid_to_iso(grid_x: int, grid_y: int) -> tuple[int, int]:
        iso_x = (grid_x - grid_y) * (RoomConfig.TILE_WIDTH // 2)
        iso_y = (grid_x + grid_y) * (RoomConfig.TILE_HEIGHT // 2)
        return iso_x, iso_y
    
    @staticmethod
    def grid_to_screen(grid_x: int, grid_y: int) -> tuple[int, int]:
        iso_x, iso_y = IsoUtils.grid_to_iso(grid_x, grid_y)
        screen_x = iso_x + RoomConfig.OFFSET_X
        screen_y = iso_y + RoomConfig.OFFSET_Y
        return screen_x, screen_y