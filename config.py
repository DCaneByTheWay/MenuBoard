"""
Configuration file for MenuBoard application.
All constants, colors, fonts, and settings in one place.
"""

# Window Settings
WINDOW_TITLE = "Positive Plates Menu Board"
WINDOW_ICON = "PositivePlatesIcon.png"

# Display Settings (optimized for 25x14 inch screen)
FONT_FAMILY = "Segoe UI"        # Clean, modern, excellent readability
TITLE_FONT_SIZE = 28            # Back to original
SECTION_FONT_SIZE = 20          # Back to original
ITEM_FONT_SIZE = 18             # Back to original
INGREDIENT_FONT_SIZE = 16       # Back to original
PRICE_FONT_SIZE = 18            # Back to original

# Colors (high contrast for readability)
BG_COLOR = "#000000"           # Black background
TEXT_COLOR = "#FFFFFF"         # White text
SECTION_COLOR = "#FFFFFF"      # White section headers
PRICE_COLOR = "#FFFFFF"        # White prices
STRIKEOUT_COLOR = "#FF0000"    # Red for sold out items
ACCENT_COLOR = "#1a1a1a"       # Very dark gray for subtle borders

# Layout Settings
SECTION_SPACING = 25           # Vertical space between sections
ITEM_SPACING = 2               # Vertical space between items within a card
CARD_PADDING = 2               # Padding inside item cards
CARD_BORDER_RADIUS = 4         # Rounded corners for cards
WINDOW_MARGINS = 10            # Margins around main window
ITEM_VERTICAL_SPACING = 0      # Vertical space between menu items

# Text Settings
MAX_LINE_LENGTH = 65             # Characters before wrapping to new line
INGREDIENT_SEPARATOR = ", "      # How to separate ingredients

# File Paths
MENU_DATA_FILE = "MenuSamples.txt"
