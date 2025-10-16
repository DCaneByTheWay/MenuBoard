"""
MenuBoard Application - Entry Point
A clean, modern menu board for Positive Plates
"""

import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MenuApp

def main():
    app = QApplication(sys.argv)
    window = MenuApp()
    
    # Show maximized for large display screens
    window.showMaximized()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
