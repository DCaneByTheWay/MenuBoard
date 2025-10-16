"""
Main window for MenuBoard application - clean and simple!
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from config import *
from ui.styles import Styles
from ui.menu_section_widget import MenuSectionWidget
from models.menu_parser import MenuParser

class MenuApp(QWidget):
    def __init__(self):
        super().__init__()
        self.menu_sections = []
        self.init_ui()
    
    def init_ui(self):
        """Initialize the main window UI"""
        # Set window properties
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.setStyleSheet(Styles.get_main_window_style())
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(WINDOW_MARGINS, WINDOW_MARGINS, WINDOW_MARGINS, WINDOW_MARGINS)
        main_layout.setSpacing(0)
        
        # Title with word wrapping
        title = 'Sat Dec 7th Menu - Vanguard Academy Craft Fair (11am-1pm)'
        title_label = QLabel(title)
        title_label.setFont(QFont(FONT_FAMILY, TITLE_FONT_SIZE, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setWordWrap(True)
        title_label.setMaximumWidth(40 * TITLE_FONT_SIZE)  # Approximately 40 characters width
        title_label.setStyleSheet(f"color: {TEXT_COLOR}; padding: 10px 0px 25px 0px;")
        
        # Center the title label
        title_container = QHBoxLayout()
        title_container.addStretch()
        title_container.addWidget(title_label)
        title_container.addStretch()
        main_layout.addLayout(title_container)
        
        # Scrollable area for menu sections
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet(f"""
            QScrollArea {{
                border: none;
                background-color: {BG_COLOR};
            }}
            QScrollBar:vertical {{
                background: {ACCENT_COLOR};
                width: 12px;
                border-radius: 6px;
            }}
            QScrollBar::handle:vertical {{
                background: #666666;
                border-radius: 6px;
            }}
        """)
        
        # Container for menu sections
        sections_container = QWidget()
        sections_layout = QVBoxLayout()
        sections_layout.setContentsMargins(0, 0, 0, 0)
        sections_layout.setSpacing(SECTION_SPACING)
        
        # Load menu data (hardcoded for now)
        self.load_menu_data()
        
        # Add each section
        for section in self.menu_sections:
            section_widget = MenuSectionWidget(section)
            sections_layout.addWidget(section_widget)
        
        sections_layout.addStretch()
        sections_container.setLayout(sections_layout)
        scroll_area.setWidget(sections_container)
        
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)
    
    def load_menu_data(self):
        """Load menu data from hardcoded dictionary (will be file later)"""
        # Copy your existing menuSections dictionary
        menu_dict = {
            "Lunch: (Add Condiments, Jalapenos, etc. $0.50 More)": [
                {"item": "Frito Chili Pie", "ingredients": ["Fritos", "Chili", "Cheese", "Onion", "Jalapeno"], "price": "$6.50"},
                {"item": "Cheese Quesadilla", "ingredients": ["Sour Cream", "Salsa"], "price": "$6.50"},
                {"item": "Chicken Quesadilla", "ingredients": ["Sour Cream", "Salsa"], "price": "$8.50"},
                {"item": "Pepperoni Quesadilla", "ingredients": ["Marinara", "Jalapeno Ranch"], "price": "$8.50"},
                {"item": "Spicy Chicken Bacon Ranch Quesadilla", "ingredients": ["Chicken", "Bacon", "Jalapenos", "Cheese", "Jalapeno Ranch", "Salsa"], "price": "$10.50"}
            ],
            "Sides": [
                {"item": "Fritos", "ingredients": [], "price": "$2.00"},
                {"item": "2 Deviled Eggs", "ingredients": ["Jalapeno", "Regular"], "price": "$3.00"},
                {"item": "2 Deviled Eggs", "ingredients": ["Bacon", "Bacon Jalapeno"], "price": "$3.50"},
                {"item": "Brown Sugar Bacon Popcorn", "ingredients": [], "price": "$4.50"}
            ],
            "Breakfast (Bacon OR Chicken)": [
                {"item": "Breakfast Quesadilla", "ingredients": ["Meat", "Egg", "Cheese", "Sour Cream", "Salsa"], "price": "$8.50"},
                {"item": "Burrito OR Sandwich OR Bowl", "ingredients": ["Meat", "Egg", "Cheese", "Tortilla", "TX Toast", "Bowl", "Salsa"], "price": "$6.40"},
                {"item": "Fruit Yogurt Granola Parfait", "ingredients": [], "price": "$6.50"}
            ],
            "Sandwiches": [
                {"item": "Spicy Chicken Bacon Ranch Grilled Cheese", "ingredients": [], "price": "$7.50"},
                {"item": "Pepperoni Pizza Melt", "ingredients": [], "price": "$6.50"},
                {"item": "Grilled Rueben", "ingredients": [], "price": "$6.50"},
                {"item": "Bacon Grilled Cheese", "ingredients": [], "price": "$6.50"},
                {"item": "Jalepeno Grilled Cheese", "ingredients": [], "price": "$6.00"},
                {"item": "Grilled Cheese", "ingredients": [], "price": "$5.50"},
                {"item": "Egg Salad Sandwich", "ingredients": [], "price": "$5.50"},
                {"item": "PB & J", "ingredients": ["Grilled OR Cold"], "price": "$5.50"}
            ],
            "Sweets": [
                {"item": "Pumpkin Bread", "ingredients": [], "price": "$3.50"},
                {"item": "2 Chocolate Peanut Butter Balls", "ingredients": [], "price": "$3.50"},
                {"item": "Big Chocolate Chip Cookie", "ingredients": [], "price": "$4.50"},
                {"item": "Snickers Tres Leches Cake", "ingredients": [], "price": "$6.50"}
            ],
            "Drinks": [
                {"item": "Smoothie", "ingredients": ['Strawberries', 'Bananas', 'Orange Juice'], "price": "$6.50"},
                {"item": "Arizona Sweet Tea", "ingredients": [], "price": "$1.50"},
                {"item": "Pop", "ingredients": ["Coke", "Cream Soda", "Diet Coke"], "price": "$1.50"},
                {"item": "Water Bottle", "ingredients": [], "price": "$1.50"}
            ]
        }
        
        # Parse using MenuParser
        self.menu_sections = MenuParser.parse_from_dict(menu_dict)
