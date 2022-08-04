# Sorting a list permanantely with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# We can also use the reverse method of sorting (also permanent)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)

# Sorting a list temporarily

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing a list in reverse order (note this is permanent)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the list, reversed:")
cars.reverse()
print(cars)

# Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
listlength = len(cars)
print(listlength)
