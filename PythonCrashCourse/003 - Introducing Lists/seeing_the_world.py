# Create a list of places I would like to visit
places = ['antarctica', 'italy', 'ireland', 'norway', 'japan']
print(places)

# Print list in alphabetical order, without modifying the original list

print("\nHere is the temporarily sorted list:")
print(sorted(places))

print("\nHere is the original list, unsorted:")
print(places)

# Print list in reverse alphabetical order, without modifying the origial list

print("\nHere is the temporarily reverse sorted list:")
print(sorted(places, reverse=True))

print("\nHere is the original list, unsorted:")
print(places)

# Use reverse to permanantely change the order of the list
places.reverse()
print(places)

# Use reverse again to permanantely change the order of the list back to the previous order
places.reverse()
print(places)

# Use sort to permanantely sort the list in alphabetical order
places.sort()
print(places)

# Use sort to reverse the alphabetical order of the list, permanantely
places.sort(reverse = True)
print(places)

