# TASK: Create an interactive grocery list manager.

# Define a function to add an item to the list
def add_item():
    new_item = iput("What item would you like to ad to the list? ")

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


# Start with an empty grocery list


# Use a loop to let the user choose an action:


# (1) Add an item


# (2) Remove an item


# (3) View the list


# (4) Exit the program


# Call the corresponding function based on user input


# Continue looping until the user chooses to exit

