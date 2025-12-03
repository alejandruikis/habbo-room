import os
from src.data.furniture_asset import FurnitureAsset
import definitions
from bs4 import BeautifulSoup
import pygame

class FurnitureExtractor:
    path: str = f"{definitions.ROOT_DIR}/src/data/furnitures/"
    xml_path: str = "xml/"
    image_path: str = "images/"
    
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
        
        return True
    
    def extract(self) -> dict[str, FurnitureAsset]:
        
        manifest_xml = self.__load_furniture_manifest_xml()
        
        if not self.__is_manifest_valid(manifest_xml):
            return None
        
        asset_xml = self.__load_furniture_asset_xml()
        visualization_xml = self.__load_furniture_visualization_xml()
        
        assets_dict = {}
        
        for asset_tag in asset_xml.find_all("asset"):
            name = asset_tag.get("name")
            flip_h = asset_tag.get("flipH") == "1"
            source = asset_tag.get("source")
            offset_x = int(asset_tag.get("x", "0"))
            offset_y = int(asset_tag.get("y", "0"))
            
            png_path = os.path.join(self.path, f"{self.image_path}{name}.png")
            sprite = None
            
            if os.path.exists(png_path):
                sprite = pygame.image.load(png_path).convert_alpha()
            
            furniture_asset = FurnitureAsset(
                flip_h=flip_h,
                type=self.furniture_type,
                offset_x=offset_x,
                offset_y=offset_y,
                source_name=source if source else "",
                sprite=sprite
            )
            
            assets_dict[name] = furniture_asset

        return assets_dict
    
