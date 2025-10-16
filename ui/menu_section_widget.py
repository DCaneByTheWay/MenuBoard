"""
MenuSectionWidget - Displays a section of menu items with a title.
"""

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from config import *
from ui.styles import Styles
from ui.menu_item_card import MenuItemCard

class MenuSectionWidget(QWidget):
    def __init__(self, menu_section, parent=None):
        super().__init__(parent)
        self.menu_section = menu_section
        self.init_ui()
    
    def init_ui(self):
        """Initialize the section UI"""
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, SECTION_SPACING)
        layout.setSpacing(ITEM_VERTICAL_SPACING)
        
        # Section title
        title_label = QLabel(self.menu_section.get_full_title())
        title_label.setFont(QFont(FONT_FAMILY, SECTION_FONT_SIZE, QFont.Bold))
        title_label.setStyleSheet(Styles.get_section_title_style())
        layout.addWidget(title_label)
        
        # Add each menu item as a card
        for menu_item in self.menu_section.items:
            item_card = MenuItemCard(menu_item)
            layout.addWidget(item_card)
        
        self.setLayout(layout)
