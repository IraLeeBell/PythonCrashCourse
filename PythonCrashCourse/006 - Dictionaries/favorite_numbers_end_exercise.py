favorite_numbers = {
	'john': [1, 23, 00],
	'jeff': [1_000_000, 143, 2],
	'paul': [42],
	'dottie': [1800, 1],
}

for name, numbers in favorite_numbers.items():
	print(f"\n{name.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}")