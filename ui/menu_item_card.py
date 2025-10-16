"""
MenuItemCard - Widget that displays a single menu item with click interactions.
"""

from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor
from config import *
from ui.styles import Styles

class MenuItemCard(QWidget):
    def __init__(self, menu_item, parent=None):
        super().__init__(parent)
        self.menu_item = menu_item
        self.ingredient_labels = []
        self.init_ui()
    
    def init_ui(self):
        """Initialize the card UI"""
        MAX_LINE_LENGTH = 65
        
        # Check if we need to wrap to a second line
        item_name = f"{self.menu_item.name}:"
        ingredients_text = self.menu_item.get_formatted_ingredients()
        total_length = len(item_name) + len(ingredients_text) + 1  # +1 for space
        
        needs_wrapping = total_length > MAX_LINE_LENGTH and self.menu_item.ingredients
        
        if needs_wrapping:
            # Two-line layout: name + price on top, ingredients on bottom
            main_layout = QVBoxLayout()
            main_layout.setContentsMargins(0, 0, 0, 0)
            main_layout.setSpacing(2)
            
            # Top row: Item name and price
            top_row = QHBoxLayout()
            top_row.setContentsMargins(0, 0, 0, 0)
            top_row.setSpacing(5)
            
            self.name_label = QLabel(item_name)
            self.name_label.setFont(QFont(FONT_FAMILY, ITEM_FONT_SIZE, QFont.Bold))
            self.name_label.setCursor(QCursor(Qt.PointingHandCursor))
            self.name_label.mousePressEvent = self.on_item_name_clicked
            top_row.addWidget(self.name_label)
            
            top_row.addStretch()
            
            self.price_label = QLabel(self.menu_item.price)
            self.price_label.setFont(QFont(FONT_FAMILY, PRICE_FONT_SIZE, QFont.Bold))
            self.price_label.setAlignment(Qt.AlignRight)
            top_row.addWidget(self.price_label)
            
            main_layout.addLayout(top_row)
            
            # Bottom row: Ingredients
            bottom_row = QHBoxLayout()
            bottom_row.setContentsMargins(0, 0, 0, 0)
            bottom_row.setSpacing(0)
            
            for idx, ingredient in enumerate(self.menu_item.ingredients):
                if idx < len(self.menu_item.ingredients) - 1:
                    ingredient_text = ingredient + ", "
                else:
                    ingredient_text = ingredient
                
                ingredient_label = QLabel(ingredient_text)
                ingredient_label.setFont(QFont(FONT_FAMILY, INGREDIENT_FONT_SIZE))
                ingredient_label.setCursor(QCursor(Qt.PointingHandCursor))
                ingredient_label.ingredient_index = idx
                ingredient_label.mousePressEvent = lambda event, lbl=ingredient_label: self.on_ingredient_clicked(lbl)
                
                self.ingredient_labels.append(ingredient_label)
                bottom_row.addWidget(ingredient_label)
            
            bottom_row.addStretch()
            main_layout.addLayout(bottom_row)
            
            self.setLayout(main_layout)
        else:
            # Single-line layout: name, ingredients, price all on one line
            card_layout = QHBoxLayout()
            card_layout.setContentsMargins(0, 0, 0, 0)
            card_layout.setSpacing(5)
            
            self.name_label = QLabel(item_name)
            self.name_label.setFont(QFont(FONT_FAMILY, ITEM_FONT_SIZE, QFont.Bold))
            self.name_label.setCursor(QCursor(Qt.PointingHandCursor))
            self.name_label.mousePressEvent = self.on_item_name_clicked
            card_layout.addWidget(self.name_label)
            
            # Ingredients on the same line
            if self.menu_item.ingredients:
                for idx, ingredient in enumerate(self.menu_item.ingredients):
                    if idx < len(self.menu_item.ingredients) - 1:
                        ingredient_text = ingredient + ", "
                    else:
                        ingredient_text = ingredient
                    
                    ingredient_label = QLabel(ingredient_text)
                    ingredient_label.setFont(QFont(FONT_FAMILY, INGREDIENT_FONT_SIZE))
                    ingredient_label.setCursor(QCursor(Qt.PointingHandCursor))
                    ingredient_label.ingredient_index = idx
                    ingredient_label.mousePressEvent = lambda event, lbl=ingredient_label: self.on_ingredient_clicked(lbl)
                    
                    self.ingredient_labels.append(ingredient_label)
                    card_layout.addWidget(ingredient_label)
            
            card_layout.addStretch()
            
            self.price_label = QLabel(self.menu_item.price)
            self.price_label.setFont(QFont(FONT_FAMILY, PRICE_FONT_SIZE, QFont.Bold))
            self.price_label.setAlignment(Qt.AlignRight)
            card_layout.addWidget(self.price_label)
            
            self.setLayout(card_layout)
        
        self.update_styles()
    
    def on_item_name_clicked(self, event):
        """Handle click on item name - toggles entire item"""
        self.menu_item.toggle_strikeout()
        self.update_styles()
    
    def on_ingredient_clicked(self, ingredient_label):
        """Handle click on individual ingredient"""
        idx = ingredient_label.ingredient_index
        self.menu_item.toggle_ingredient_strikeout(idx)
        self.update_styles()
    
    def update_styles(self):
        """Update visual styles based on strikeout state"""
        # Update card border if item is struck out
        self.setStyleSheet(Styles.get_item_card_style(self.menu_item.is_struck_out))
        
        # Update item name
        name_font = self.name_label.font()
        name_font.setStrikeOut(self.menu_item.is_struck_out)
        self.name_label.setFont(name_font)
        self.name_label.setStyleSheet(Styles.get_item_name_style(self.menu_item.is_struck_out))
        
        # Update price
        price_font = self.price_label.font()
        price_font.setStrikeOut(self.menu_item.is_struck_out)
        self.price_label.setFont(price_font)
        self.price_label.setStyleSheet(Styles.get_price_style(self.menu_item.is_struck_out))
        
        # Update each ingredient
        for idx, ingredient_label in enumerate(self.ingredient_labels):
            is_struck = self.menu_item.is_ingredient_struck_out(idx) or self.menu_item.is_struck_out
            
            ing_font = ingredient_label.font()
            ing_font.setStrikeOut(is_struck)
            ingredient_label.setFont(ing_font)
            ingredient_label.setStyleSheet(Styles.get_ingredient_style(is_struck))
