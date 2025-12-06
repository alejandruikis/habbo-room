from typing import List, Optional

from src.objects.furniture.furniture import Furniture


class FurnitureSelector:
    
    def __init__(self, furnitures: List[Furniture]):
        self.furnitures = furnitures
        self.selected: Optional[Furniture] = None
    
    def handle_click(self, mouse_pos: tuple) -> bool:
        previous_selection = self.selected
        self.selected = None
        
        for furniture in self.furnitures:
            if furniture.get_rect().collidepoint(mouse_pos):
                self.selected = furniture
                break
        
        return self.selected != previous_selection