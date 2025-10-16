"""
MenuItem class - represents a single menu item with ingredients and price.
"""

class MenuItem:
    def __init__(self, name, ingredients=None, price="", section=""):
        """
        Initialize a menu item.
        
        Args:
            name (str): Item name (e.g., "Frito Chili Pie")
            ingredients (list): List of ingredient strings
            price (str): Price string (e.g., "$6.50")
            section (str): Section this item belongs to
        """
        self.name = name
        self.ingredients = ingredients if ingredients else []
        self.price = price
        self.section = section
        
        # Track strikethrough state
        self.is_struck_out = False
        self.struck_ingredients = set()  # Set of ingredient indices that are struck out
    
    def toggle_strikeout(self):
        """Toggle the entire item's strikeout state."""
        self.is_struck_out = not self.is_struck_out
        
        # If striking out entire item, mark all ingredients as struck
        if self.is_struck_out:
            self.struck_ingredients = set(range(len(self.ingredients)))
        else:
            self.struck_ingredients.clear()
    
    def toggle_ingredient_strikeout(self, ingredient_index):
        """Toggle strikeout for a specific ingredient."""
        if ingredient_index in self.struck_ingredients:
            self.struck_ingredients.remove(ingredient_index)
        else:
            self.struck_ingredients.add(ingredient_index)
    
    def is_ingredient_struck_out(self, ingredient_index):
        """Check if a specific ingredient is struck out."""
        return ingredient_index in self.struck_ingredients
    
    def get_formatted_ingredients(self):
        """Return ingredients as a comma-separated string."""
        if not self.ingredients:
            return ""
        return ", ".join(self.ingredients)
    
    def __repr__(self):
        return f"MenuItem(name='{self.name}', price='{self.price}', ingredients={len(self.ingredients)})"
