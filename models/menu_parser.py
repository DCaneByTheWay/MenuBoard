"""
MenuParser - Parses menu data from file or dictionary.
Handles the MenuSamples.txt file format.
"""

from models.menu_item import MenuItem
from models.menu_section import MenuSection
import re

class MenuParser:
    
    @staticmethod
    def parse_from_dict(menu_dict):
        """
        Parse menu from the existing dictionary format.
        
        Args:
            menu_dict (dict): Dictionary with section names as keys
        
        Returns:
            list: List of MenuSection objects
        """
        sections = []
        
        for section_title, items in menu_dict.items():
            # Parse section title and subtitle
            title, subtitle = MenuParser._parse_section_title(section_title)
            section = MenuSection(title, subtitle)
            
            # Add items to section
            for item_data in items:
                menu_item = MenuItem(
                    name=item_data["item"],
                    ingredients=item_data.get("ingredients", []),
                    price=item_data.get("price", "")
                )
                section.add_item(menu_item)
            
            sections.append(section)
        
        return sections
    
    @staticmethod
    def _parse_section_title(full_title):
        """
        Parse section title to separate main title from subtitle.
        
        Example: "Lunch: (Add Condiments...)" -> ("Lunch", "Add Condiments...")
        """
        # Match pattern: "Title: (Subtitle)" or "Title (Subtitle)"
        match = re.match(r'^([^:(]+)(?::\s*)?(?:\(([^)]+)\))?', full_title)
        
        if match:
            title = match.group(1).strip()
            subtitle = match.group(2).strip() if match.group(2) else ""
            return title, subtitle
        
        return full_title.strip(), ""
    
    @staticmethod
    def parse_from_file(filepath):
        """
        Parse menu from MenuSamples.txt file.
        TODO: Implement file parsing based on your file format.
        
        Args:
            filepath (str): Path to menu data file
        
        Returns:
            list: List of MenuSection objects
        """
        # This will be implemented once we examine MenuSamples.txt format
        raise NotImplementedError("File parsing not yet implemented")
