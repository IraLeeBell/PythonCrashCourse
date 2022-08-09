requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"\nSorry, we are out of {requested_topping} right now.")
    else:
        print(f"\nAdding {requested_topping}.")

# Checking that a list is not empty

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"\nAdding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")

# Using multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"\nAdding {requested_topping}.")
    else:
        print(f"\nI'm sorry, we don't have {requested_topping}")
print("\nFinished making your pizza!")