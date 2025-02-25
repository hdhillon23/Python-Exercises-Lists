# TASK: Create an interactive grocery list manager.

# Define a function to add an item to the list
def add_item():
    new_item = input("What item would you like to ad to the list? ")

# Append the item to the list and return it
    grocery_list.append(new_item)

# Define a function to remove an item from the list
def remove_item():
    eliminate = input("What item would you like to remove from the grocery list? ")

# If the item exists, remove it
    if eliminate in grocery_list:
        grocery_list.remove(eliminate)

# If not, display a message saying the item is not in the list
    else:
        print("Your given item is already not in the list!")

# Define a function to display the grocery list
def show_list():

# If the list is not empty, print all items with numbers
    for item in grocery_list:
        print(item)

# If the list is empty, display a message
    if not grocery_list:
        print(item)

def bye():
    exit()

# Start with an empty grocery list
grocery_list = []

# Use a loop to let the user choose an action:

while True:
    user_input = input("What would you like to do with the grocery list [add item], [remove item], [show list] or [exit] ").strip().lower()

# (1) Add an item

    if user_input == "add item":
        add_item()
        print("This is your updated grocery list")
        show_list()

# (2) Remove an item

    elif user_input == "remove item":
        remove_item()
        print("This is you updated grocery list")
        show_list()

# (3) View the list

    elif user_input == "show list":
        show_list()

# (4) Exit the program

    elif user_input == "exit":
        bye()
    else:
        print("Please Enter a Valid option, to exit simply type exit")