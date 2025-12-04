from src.data.furniture import Furniture
from src.data.furniture_extractor import FurnitureExtractor


class FurnitureRegistry:
    
    _instance = None
    _furniture_cache: dict[str, Furniture] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def load_furniture(cls, furniture_type: str) -> Furniture:
        if furniture_type in cls._furniture_cache:
            print(f"{furniture_type} from cache")
            return cls._furniture_cache[furniture_type]
        
        extractor = FurnitureExtractor(furniture_type)
        furniture = extractor.extract()
        
        if furniture:
            cls._furniture_cache[furniture_type] = furniture
            return furniture
        else:
            return None
    
    @classmethod
    def preload_all(cls, furniture_types: list[str]):
        for furniture_type in furniture_types:
            cls.load_furniture(furniture_type)