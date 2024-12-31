import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontMetrics, QIcon

class MenuApp(QWidget):
                
    def __init__(self):
        super().__init__()
        self.initUI()
        
    # given layout, removes last added item
    def removeLastItemFromLayout(self, layout):

        # get count
        count = layout.count()

        if count > 0:

            # get last item
            item = layout.takeAt(count - 1)

            # get widget from item
            widget = item.widget()

            # delete widget if it exists
            if widget is not None:
                widget.deleteLater()

    def initUI(self):

        # font size for non title text
        fontsize = 18

        # main window layout
        mainLayout = QVBoxLayout()

        # set background color to black and text color to white
        self.setStyleSheet("background-color: black; color: white;")

        # title label
        menuTitle = 'Sat Dec 7th Menu - Vanguard Academy Craft Fair (11am-1pm)'
        titleLabel = QLabel(menuTitle)
        titleFont = QFont("Arial", fontsize + 4, QFont.Bold)
        titleLabel.setFont(titleFont)
        titleLabel.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(titleLabel)

        # hard coded menu sections (for now), will implement file parsing
        self.menuSections = {
            "Lunch: (Add Condiments, Jalapenos, etc. $0.50 More)": [
                {"item": "Frito Chili Pie", "ingredients": ["Fritos", "Chili", "Cheese", "Onion", "Jalapeno"], "price": "$6.50"},
                {"item": "Cheese Quesadilla", "ingredients": ["Sour Cream", "Salsa"], "price": "$6.50"},
                {"item": "Chicken Quesadilla", "ingredients": ["Sour Cream", "Salsa"], "price": "$8.50"},
                {"item": "Pepperoni Quesadilla", "ingredients": ["Marinara", "Jalapeno Ranch"], "price": "$8.50"},
                {"item": "Spicy Chicken Bacon Ranch Quesadilla", "ingredients": ["Chicken", "Bacon", "Jalapenos", "Cheese", "Jalapeno Ranch", "Salsa"], "price": "$10.50"},
                {"item": "Chicken Quesadilla", "ingredients": ["Sour Cream", "Salsa"], "price": "$8.50"},
                {"item": "Spicy Chicken Bacon Ranch Quesadilla", "ingredients": ["Chicken", "Bacon", "Jalapenos", "Cheese", "Jalapeno Ranch", "Salsa"], "price": "$10.50"},
                {"item": "NO INGREDIENTS ITEM", "ingredients": [], "price": "$99.50"},
                {"item": "Chicken Quesadilla", "ingredients": ["Sour Cream", "Salsa"], "price": "$8.50"}
            ],
            "Sides": [
                {"item": "Fritos", "ingredients": [], "price": "$2.00"},
                {"item": "2 Deviled Eggs", "ingredients": ["Jalapeno", "Regular"], "price": "$3.00"},
                {"item": "2 Deviled Eggs", "ingredients": ["Bacon", "Bacon Jalapeno"], "price": "$3.50"},
                {"item": "Brown Sugar Bacon Popcorn", "ingredients": [], "price": "$4.50"}
            ],
            "Drinks": [
                {"item": "Smoothie", "ingredients": ['Strawberries', 'Bananas', 'Orange Juice'], "price": "$6.50"},
                {"item": "Arizona Sweet Tea", "ingredients": [], "price": "$1.50"},
                {"item": "Pop", "ingredients": ["Coke", "Cream Soda", "Diet Coke"], "price": "$1.50"},
                {"item": "Water Bottle", "ingredients": [], "price": "$1.50"}
            ]
        }

        # fonts used
        sectionFont = QFont("Arial", fontsize, QFont.Bold)
        itemFont = QFont("Arial", fontsize, QFont.Bold)
        ingredientFont = QFont("Arial", fontsize)

        # create and populate sections
        for section, items in self.menuSections.items():
           
            # include space before each section
            mainLayout.addSpacerItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

            # section title
            sectionLabel = QLabel(section)
            sectionLabel.setFont(sectionFont)
            sectionLabel.setAlignment(Qt.AlignLeft)
            sectionLabel.setStyleSheet("text-decoration: underline;")
            mainLayout.addWidget(sectionLabel)

            # grid layout for section items
            gridLayout = QGridLayout()

            # variable to maintain row displacement due to ingredient wrapping to next line
            rowDisplacement = 0

            # iterate through items and add to grid layout
            for row, menu in enumerate(items):

                item = menu["item"]
                price = menu["price"]

                #print(f'CURRENT ITEM: {item}')

                # item name label
                itemLabel = QLabel(item)
                itemLabel.setFont(itemFont)
                itemLabel.setCursor(Qt.PointingHandCursor)
                #itemLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
                fm = QFontMetrics(itemLabel.font())
                #itemLabel.setFixedWidth(fm.width(itemLabel.text()) + 15)
                #itemLabel.setStyleSheet("background-color: yellow; border: 2px solid red;")
                itemLabel.setAlignment(Qt.AlignLeft)

                # let item label toggle strikethrough on mouse click
                itemLabel.mousePressEvent = lambda event, label=itemLabel, menu=menu: self.toggleItemStrikethrough(label, menu)

                # sub layout for ingredients of item
                ingredientLayout = QHBoxLayout()
                ingredientLayout.addWidget(itemLabel)
                overflowIngredientLayout = QHBoxLayout()

                # current length of all text
                currentLength = len(item) + len(price)

                # max length of string before word wrap (i am very funny)
                magicNumber = 80

                # boolean to keep track of ingredients, false by default
                hasIngredients = False

                # iterate through ingredients and create label for each
                for idx, ingredient in enumerate(menu["ingredients"]):

                    # item has ingredients if we are in the loop
                    hasIngredients = True

                    # add ingredient name to current length
                    currentLength += len(ingredient)

                    ingredientLabel = QLabel(ingredient)
                    ingredientLabel.setFont(ingredientFont)
                    ingredientLabel.setAlignment(Qt.AlignLeft)
                    ingredientLabel.setCursor(Qt.PointingHandCursor)
                    #ingredientLabel.setFixedWidth(len(ingredient) * 10)
                    fm = QFontMetrics(ingredientLabel.font())
                    #ingredientLabel.setFixedWidth(fm.width(ingredientLabel.text()) + 15)
                    #ingredientLabel.setStyleSheet("background-color: orange; border: 2px solid red;")


                    # let ingredient label toggle strikethrough on mouse click
                    ingredientLabel.mousePressEvent = lambda event, label=ingredientLabel, menu=menu: self.toggleIngredientStrikethrough(label, menu)


                    # if over max char length
                    # add ingredient label to ingredient overflow layout (drop ingredients to next line)
                    if currentLength > magicNumber: 

                        overflowIngredientLayout.addWidget(ingredientLabel)
                        
                        # create and add label for comma to separate labels
                        commaLabel = QLabel(',')
                        #commaLabel.setStyleSheet("background-color: orange; border: 2px solid red;")
                        commaLabel.setFixedWidth(20)
                        overflowIngredientLayout.addWidget(commaLabel)

                    # else, add ingredient label to ingredient layout
                    else:

                        ingredientLayout.addWidget(ingredientLabel)

                        # create and add label for comma to separate labels
                        commaLabel = QLabel(',')
                        #commaLabel.setStyleSheet("background-color: orange; border: 2px solid red;")
                        commaLabel.setFixedWidth(20)
                        ingredientLayout.addWidget(commaLabel)

                    # store the ingredient label in the menu dict for later toggling
                    if "ingredientLabels" not in menu:
                        menu["ingredientLabels"] = []
                    menu["ingredientLabels"].append(ingredientLabel)

                # price label, right aligned
                priceLabel = QLabel(price)
                priceLabel.setFont(itemFont)
                priceLabel.setAlignment(Qt.AlignRight)

                # store the price label in the menu dict for later toggling
                menu["priceLabel"] = priceLabel

                # add the ingredientLayout and priceLabel to the grid layout
                # account for row displacement in case of word wrap due to char limit
                gridLayout.addLayout(ingredientLayout, row + rowDisplacement, 0)
                gridLayout.addWidget(priceLabel, row + rowDisplacement, 2)
                if currentLength > magicNumber:
                    rowDisplacement += 1
                    gridLayout.addLayout(overflowIngredientLayout, row + rowDisplacement, 0)

                    if hasIngredients: # if there are ingredients (so we use commas), remove comma
                        self.removeLastItemFromLayout(overflowIngredientLayout)
                else:
                    if hasIngredients: # if there are ingredients (so we use commas), remove comma
                        self.removeLastItemFromLayout(ingredientLayout)

            # add the grid layout to the main layout
            mainLayout.addLayout(gridLayout)

        # set the main layout for the window
        self.setLayout(mainLayout)

        # set window properties
        self.setWindowTitle('Positive Plates Menu Application')
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon('PositivePlatesIcon.png'))

    # toggle strikethrough for the entire item (item + ingredients + price)
    def toggleItemStrikethrough(self, label, menu):
        itemFont = label.font()

        # strikeout to default
        if itemFont.strikeOut():
            itemFont.setStrikeOut(False)
            label.setStyleSheet('color: white;')
            menu["priceLabel"].setStyleSheet('color: white;')
            priceFont = menu["priceLabel"].font()
            priceFont.setStrikeOut(False)
            menu["priceLabel"].setFont(priceFont)
        # default to strikeout
        else:
            itemFont.setStrikeOut(True)
            label.setStyleSheet('color: red;')
            menu["priceLabel"].setStyleSheet('color: red;')
            priceFont = menu["priceLabel"].font()
            priceFont.setStrikeOut(True)
            menu["priceLabel"].setFont(priceFont)

        # iterate through ingredients in item and toggle strikeout
        if "ingredientLabels" in menu:

            for ingredientLabel in menu["ingredientLabels"]:
                ingredientFont = ingredientLabel.font()

                # strikeout to default
                if itemFont.strikeOut():
                    ingredientFont.setStrikeOut(True)
                    ingredientLabel.setStyleSheet('color: red;')
                # default to strikeout
                else:
                    ingredientFont.setStrikeOut(False)
                    ingredientLabel.setStyleSheet('color: white;')
                ingredientLabel.setFont(ingredientFont)

        # apply changes
        label.setFont(itemFont)

    # toggle strikethrough for the individual ingredient
    def toggleIngredientStrikethrough(self, label, menu):
        font = label.font()

        # strikeout to default
        if font.strikeOut():
            font.setStrikeOut(False)
            label.setStyleSheet('color: white;')
        # default to strikeout
        else:
            font.setStrikeOut(True)
            label.setStyleSheet('color: red;')
        label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MenuApp()
    ex.show()
    sys.exit(app.exec_())
