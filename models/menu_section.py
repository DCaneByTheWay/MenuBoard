"""
MenuSection class - represents a section of the menu (e.g., "Lunch", "Sides").
"""

class MenuSection:
    def __init__(self, title, subtitle=""):
        """
        Initialize a menu section.
        
        Args:
            title (str): Section title (e.g., "Lunch")
            subtitle (str): Optional subtitle (e.g., "Add Condiments, Jalapenos, etc. $0.50 More")
        """
        self.title = title
        self.subtitle = subtitle
        self.items = []
    
    def add_item(self, menu_item):
        """Add a MenuItem to this section."""
        menu_item.section = self.title
        self.items.append(menu_item)
    
    def get_full_title(self):
        """Get the complete title including subtitle."""
        if self.subtitle:
            return f"{self.title}: ({self.subtitle})"
        return self.title
    
    def __repr__(self):
        return f"MenuSection(title='{self.title}', items={len(self.items)})"
