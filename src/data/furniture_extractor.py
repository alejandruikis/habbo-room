import os
import pprint
import re
from typing import List
from src.objects.furniture.furniture_base import FurnitureBase
from src.data.furniture_layer import FurnitureLayer
from src.data.furniture_asset import FurnitureAsset
import definitions
from bs4 import BeautifulSoup
import pygame

from src.utils import xml_layer

class FurnitureExtractor:
    path: str = f"{definitions.ROOT_DIR}/src/data/furnitures/"
    xml_path: str = "xml/"
    image_path: str = "images/"
    possible_furniture_directions: List[int] = [2, 4, 6, 0]
    actual_furniture_directions: List[int] = []
    
    def __init__(self, furniture_type: str):
        self.furniture_type = furniture_type
        self.__set_path(furniture_type)
    
    def __set_path(self, furniture_type: str):
        self.path = os.path.join(self.path, f"{furniture_type}/")
        self.xml_path = os.path.join(self.path, self.xml_path)
    
    def __load_furniture_manifest_xml(self) -> BeautifulSoup:
        with open(os.path.join(self.path, f"{self.xml_path}{self.furniture_type}_manifest.xml"), "r", encoding="utf-8") as file:
            content = file.read()
        return BeautifulSoup(content, "xml")
    
    def __load_furniture_asset_xml(self) -> BeautifulSoup:
        with open(os.path.join(self.path, f"{self.xml_path}{self.furniture_type}_assets.xml"), "r", encoding="utf-8") as file:
            content = file.read()
        return BeautifulSoup(content, "xml")
    
    def __load_furniture_visualization_xml(self) -> BeautifulSoup:
        with open(os.path.join(self.path, f"{self.xml_path}{self.furniture_type}_visualization.xml"), "r", encoding="utf-8") as file:
            content = file.read()
        return BeautifulSoup(content, "xml")
    
    def __is_manifest_valid(self, soup: BeautifulSoup) -> bool:
        # Check if furniture has assets and visualization xml
        if soup.find("asset", {"name": f"{self.furniture_type}_visualization"}) is None:
            return False
        
        if soup.find("asset", {"name": f"{self.furniture_type}_assets"}) is None:
            return False
        
        if soup.find("asset", {"name": f"{self.furniture_type}_logic"}) is None:
            return False
        
        return True
    
    def extract(self) -> FurnitureBase:
        
        manifest_xml = self.__load_furniture_manifest_xml()
        
        if not self.__is_manifest_valid(manifest_xml):
            return None
        
        # Get XML
        logic_xml = self.__load_furniture_logic_xml()
        self.actual_furniture_directions = self.__extract_possible_directions(logic_xml)

        if len(self.actual_furniture_directions) == 0:
            print(f"WARNING: Furniture '{self.furniture_type}' does not have any direction!")

        asset_xml = self.__load_furniture_asset_xml()
        visualization_xml = self.__load_furniture_visualization_xml()
        dimensions = self.__extract_dimension(logic_xml)
        

        # Extracting
        asset_dic = self.__extract_furniture_assets(asset_xml)
        furniture_layers = self.__build_furniture_layers(visualization_xml, asset_dic)

        return FurnitureBase(name=self.furniture_type,
                         tile_width=int(dimensions["x"]),
                         tile_height=int(dimensions["y"]),
                         layers=furniture_layers,
                         all_assets=asset_dic,
                         possible_directions=self.actual_furniture_directions
        )
    
    def __extract_possible_directions(self, logic_xml) -> List[int]:

        directions_tag = logic_xml.find("directions")
        if directions_tag:
                direction_tags = directions_tag.find_all("direction")
                self.directions_count = len(direction_tags)

        direction_count = self.directions_count if self.directions_count > 0 else len(self.possible_furniture_directions)
        direction_count = min(direction_count, len(self.possible_furniture_directions))
        
        return self.possible_furniture_directions[:direction_count]
 
    def __extract_dimension(self, logic_xml) -> dict:
        dimensions_tag = logic_xml.find("dimensions")
    
        if dimensions_tag:
            return {
                'x': int(dimensions_tag.get('x')),
                'y': int(dimensions_tag.get('y')),
                'z': float(dimensions_tag.get('z'))
            }
        
        return {'x': 1, 'y': 1, 'z': 1.0}

    def __load_furniture_logic_xml(self) -> BeautifulSoup:
        with open(os.path.join(self.path, f"{self.xml_path}{self.furniture_type}_logic.xml"), "r", encoding="utf-8") as file:
            content = file.read()
        return BeautifulSoup(content, "xml")

    def __build_furniture_layers(self, 
                                 visualization_xml: BeautifulSoup,
                                 asset_dict: dict[str, FurnitureAsset],
                                 is_multistate: bool = False) -> list[FurnitureLayer]:
    
        viz_64 = visualization_xml.find("visualization", {"size": "64"})
        
        if not viz_64:
            return []
        
        layer_data = self.__extract_layer_data(viz_64)
        layer_data = self.__extract_directions_data(viz_64, layer_data)
        layer_data = self.__extract_layer_z_index(viz_64, layer_data)
        
        furniture_layers = []
        
        for layer_id, directions_dict in layer_data.items():
            z_index = list(directions_dict.values())[0]
            layer_letter = xml_layer.LAYER_ID_TO_LETTER.get(layer_id, "a")
            
            layer_assets = {}
            
            for direction in directions_dict.keys():
                layer_assets[direction] = []

                for i in range(1): # collect animation frame assets
                    asset_name = f"{self.furniture_type}_64_{layer_letter}_{direction}_{i}"
                    asset = asset_dict.get(asset_name)

                    if asset:
                        layer_assets[direction].append(asset)
                    

            furniture_layer = FurnitureLayer(
                layer_id=layer_id,
                type=self.furniture_type,
                z_index=z_index,
                assets=layer_assets
            )
            
            furniture_layers.append(furniture_layer)
        
        furniture_layers.sort(key=lambda l: l.z_index)
        #pprint.pp(furniture_layers)
        return furniture_layers
    
    def __extract_layer_data(self, viz_64) -> dict:
        layer_data = {}
        z_index = 0

        layers_tag = viz_64.find("layers")
        if layers_tag:
            for layer_tag in layers_tag.find_all("layer"):
                layer_id = int(layer_tag.get("id"))

                if(layer_tag.get("z") is not None):
                    z_index = int(layer_tag.get("z"))
                
                for direction in self.actual_furniture_directions:
                    if layer_id not in layer_data:
                        layer_data[layer_id] = {}
                    layer_data[layer_id][direction] = z_index

        return layer_data

    def __extract_directions_data(self, viz_64, layer_data) -> dict:
        directions_tag = viz_64.find("directions")
        if directions_tag:
            for direction_tag in directions_tag.find_all("direction"):
                direction_id = int(direction_tag.get("id"))
                
                for layer_tag in direction_tag.find_all("layer"):
                    layer_id = int(layer_tag.get("id"))
                    z_index = int(layer_tag.get("z"))
                    
                    if layer_id not in layer_data:
                        layer_data[layer_id] = {}
                    layer_data[layer_id][direction_id] = z_index

        return layer_data

    def __extract_layer_z_index(self, viz_64, layer_data) -> dict:
        z_index = 0 
        layer_count = int(viz_64.get("layerCount"))

        for layer_id in range(layer_count):
            if layer_id not in layer_data:
                layer_data[layer_id] = {}
                for direction in self.actual_furniture_directions:
                    layer_data[layer_id][direction] = z_index

        return layer_data

    def __extract_furniture_assets(self, asset_xml) -> dict[str, FurnitureAsset]:
        assets_dict = {}

        for asset_tag in asset_xml.find_all("asset"):
            name = asset_tag.get("name")
            flip_h = asset_tag.get("flipH") == "1"
            source = asset_tag.get("source")
            offset_x = int(asset_tag.get("x", "0"))
            offset_y = int(asset_tag.get("y", "0"))
            sprite = None
            png_path = os.path.join(self.path, f"{self.image_path}{name}.png")
            
            regex = re.search(r'_(\d+)$', name or "")
            frame = int(regex.group(1)) if regex else 0

            if os.path.exists(png_path):
                sprite = pygame.image.load(png_path).convert_alpha()
            
            furniture_asset = FurnitureAsset(
                name=name,
                flip_h=flip_h,
                type=self.furniture_type,
                offset_x=offset_x,
                offset_y=offset_y,
                source_name=source if source else name,
                sprite=sprite,
                frame=frame
            )

            assets_dict[name] = furniture_asset

        return assets_dict