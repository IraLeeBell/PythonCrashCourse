dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

print("Original dimension:")
for dimension in dimensions:
	print(dimension)

# Though you can't write over a tuple, you can assign a whole new value to a variable which represents a tuple
dimensions = (400, 100)
print("New dimension")
for dimension in dimensions:
	print(dimension)
