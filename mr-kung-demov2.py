"""
    Create a list of cars and allow the user to take an item out using the index number.
"""

# Create a list of 3 cars
cars = ["Bmw", "Honda", "Toyota"]

# Print the list of cars
for car in cars:
    print(car)

# Ask the user which car to remove (index number)
cars.remove(input("What car would you like to remove? ").strip().title())
            
# remove that car and print out the new list
print("Here's the new list:")
for car in cars:
    print(car)