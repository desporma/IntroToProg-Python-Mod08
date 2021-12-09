# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# DEsporma,12.7.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
list_of_products = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price

    methods:
        __str__(self): return string of product_name and product_price separated by "|"

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DEsporma,12.8.2021,Modified code to complete assignment 8
    """

    # Constructor:
    def __init__(self, product_name, product_price):
        # Attributes
        self.__product_name = str(product_name)
        self.__product_price = float(product_price)

    # Properties:
    # Product Name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value: str):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Please do not enter numbers.")

    # Product Price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):
        if str(value).isnumeric() == True:
            self.__product_price = float(value)
        else:
            raise Exception("Please only enter numbers.")

    # Methods:
    def __str__(self):
        return self.product_name + "|" + str(self.product_price)


# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        read_data_from_file(file_name): -> (a list of product objects)
        write_data_to_file(file_name, list_of_product_objects):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DEsporma,12.8.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name):
        list_of_products.clear()
        file = open(file_name, "r")
        for line in file:
            product, price = line.split("|")
            product = str(product.strip())
            price = float(price.strip())
            row = Product(product, price)
            list_of_products.append(row)
        file.close()
        return list_of_products

    # TODO: Add Code to process data to a file
#    @staticmethod
#    def add_data_to_list(product, price, list_of_products):
#        row = Product(product,price).product_name, Product(product,price).product_price
#        list_of_products.append(row)

    @staticmethod
    def write_data_to_file(file_name):
        file = open(file_name, "w")
        for row in list_of_products:
            file.write(row.__str__() + "\n")
        file.close()

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Presents user with options for interaction with data.

    methods:
        print_menu_Products():
        Show menu to user

        input_menu_choice():
        Ask user for selection from menu

        print_current_Products_in_list():
        Show current product list to user

        input_new_product_and_price():
        Add item to list

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DEsporma,12.8.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def print_menu_Products():
        print('''
        Menu of Options
        1) Show current products 
        2) Add a new product to list
        3) Save data to file        
        4) Exit program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Products_in_list(list_of_products):
        print("*******The current products listed are:*******")
        print("Product | Price")
        for line in list_of_products:
            print(line.product_name + " | $" + str(line.product_price))
        print("**********************************************")
        print() # Add an extra line for looks

    @staticmethod
    def input_new_product_and_price():
        product = str(input("Please enter a product: ")).strip()
        price = str(input("Please enter a price: "))
        userdata = Product(product_name=product, product_price=price)
        return userdata

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while(True):
    # Show user a menu of options
    IO.print_menu_Products()

    # Get user's menu option choice
    usrchoice = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if usrchoice == "1":
        IO.print_current_Products_in_list(lstOfProductObjects)

    # Let user add data to the list of product objects
    elif usrchoice == "2":
        list_of_products.append(IO.input_new_product_and_price())
        print("Products added!")

    # Let user save current data to file
    elif usrchoice == "3":
        FileProcessor.write_data_to_file(strFileName)
        print("Data saved!")

    # Let user exit program
    elif usrchoice == "4":
        print("Program successfully exited.")
        break

    continue

# Main Body of Script  ---------------------------------------------------- #