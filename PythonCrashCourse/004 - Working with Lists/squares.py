squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)

print(squares)

# The below code procudes the same result but is writen more concisely

squares = []
for value in range(1,11):
	squares.append(value ** 2)

print(squares)


# The below code does the same thing, but is known as a 'list comprehension'

squares = [value ** 2 for value in range(1,11)]
print(squares)
