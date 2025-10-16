"""
Centralized styling for MenuBoard UI components.
"""

from config import *

class Styles:
    """CSS-like styles for Qt widgets"""
    
    @staticmethod
    def get_main_window_style():
        """Main window background style"""
        return f"""
            QWidget {{
                background-color: {BG_COLOR};
                color: {TEXT_COLOR};
            }}
        """
    
    @staticmethod
    def get_section_title_style():
        """Section header style"""
        return f"""
            QLabel {{
                color: {SECTION_COLOR};
                text-decoration: underline;
                padding: 5px 0px 3px 0px;
            }}
        """
    
    @staticmethod
    def get_item_card_style(is_struck_out=False):
        """Individual menu item card style"""
        return f"""
            QWidget {{
                background-color: transparent;
                border: none;
                padding: {CARD_PADDING}px 0px;
                margin: 0px;
            }}
        """
    
    @staticmethod
    def get_item_name_style(is_struck_out=False):
        """Item name label style"""
        color = STRIKEOUT_COLOR if is_struck_out else TEXT_COLOR
        return f"""
            QLabel {{
                color: {color};
                background-color: transparent;
                border: none;
            }}
        """
    
    @staticmethod
    def get_ingredient_style(is_struck_out=False):
        """Ingredient label style"""
        color = STRIKEOUT_COLOR if is_struck_out else TEXT_COLOR
        return f"""
            QLabel {{
                color: {color};
                background-color: transparent;
                border: none;
            }}
        """
    
    @staticmethod
    def get_price_style(is_struck_out=False):
        """Price label style"""
        color = STRIKEOUT_COLOR if is_struck_out else PRICE_COLOR
        return f"""
            QLabel {{
                color: {color};
                background-color: transparent;
                border: none;
            }}
        """
