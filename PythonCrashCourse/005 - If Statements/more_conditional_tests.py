# Tests for equality and inequality with strings

car = 'porsche'
if car == 'porsche':
    print(f"\nThe car is a {car.title()}.")
else:
    print("\nThe car is not a porsche.")

if car != 'volvo':
    print("\nThe two cars do not match.")
else:
    print("\nThe two cars match.")

# Tests using the lower() method

weather = 'Sunny'
if weather.lower() == 'sunny':
    print(f"\nToday will be {weather}")
else:
    print(f"\nToday will not be {weather}")

# Numerical tests involving equality and inequality, greater than and less than,
# greater than or equal to, and less than or equal to

building_one_length = 20
building_two_length = 10
building_three_length = 40

if building_three_length == 40:
    print(f"\nThe length of building three is {building_three_length}")
else:
    print(f"\nThe length of building three does not equal {building_three_length}")

if building_two_length > building_one_length:
    print(f"\nSince building two is {building_two_length} feet and building one is {building_one_length} feet, building two is longer than building one.")
else:
    print(f"\nSince building two is {building_two_length} feet and building one is {building_one_length} feet, building two is shorter than building one.")

if building_one_length + building_two_length < building_three_length:
    print("\nBuilding one and two together are still less than the length of building three.")
else:
    print("\nBuilding one and two together are not less than the length of building three.")

if building_one_length + building_two_length + building_three_length <= 100:
    print("\nBuilding one, two and three together are less than or equal to 100.")
else:
    print("\nBuilding one, two and three together are not less than or equal to 100.")

if building_one_length + building_two_length + building_three_length >= 70:
    print("\nBuilding one, two and three together are greater than or equal to 70.")
else:
    print("\nBuilding one, two and three toghether are not greater than or equal to 70.")

# Tests using the and keyword and the or keyword

colors_one = ['red', 'green', 'blue']
colors_two = ['red', 'white', 'blue']

color = 'red'
if color in colors_one and color in colors_two:
    print(f"\n{color.title()} appears in both lists.")
else:
    print(f"\n{color.title()} does not appear in both lists.")

color = 'white'
if color in colors_one or color in colors_two:
    print(f"\n{color.title()} appears in at least one of the lists.")
else:
    print(f"\n{color.title()} does not appear in at least one of the lists.")

# Test whether an item is in a list

colors = ['red', 'green', 'blue', 'white']
color = 'white'

if color in colors:
    print(f"\n{color.title()} is in the list.")
else:
    print(f"\n{color.title()} is not in the list.")

# Test whether an item is not in a list

colors = ['red', 'green', 'blue', 'orange']
color = 'yellow'

if color not in colors:
    print(f"\n{color.title()} is not in the list")
else:
    print(f"\n{color.title()} is in the the list.")