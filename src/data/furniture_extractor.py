import os
import definitions
from bs4 import BeautifulSoup


class FurnitureExtractor:
    path: str = f"{definitions.ROOT_DIR}/src/data/furniture/"

    def __init__(self, type: str):
        self.type = type

        self.set_path(type)

    def set_path(self, type: str):
        self.path = os.path.join(self.path, f"{type}.xml")

    

    
