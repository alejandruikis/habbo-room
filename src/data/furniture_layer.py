from src.data.furniture_asset import FurnitureAsset
from src.utils.xml_layer import get_layer_id_from_letter

class FurnitureLayer:
    layer_id: int
    type: str
    z_index: int
    assets: dict[int, FurnitureAsset] # int -> direction

    def __init__(self, layer_id: int, z_index: int = 0):
        self.layer_id = layer_id
        self.z_index = z_index
        self.assets = {}

    @staticmethod
    def get_layer_id_from_letter(letter: str) -> int:
        return get_layer_id_from_letter(letter)

    def add_asset_to_layer(self, direction_id: int, asset: FurnitureAsset):
        self.assets[direction_id] = asset