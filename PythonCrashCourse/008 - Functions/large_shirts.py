def make_shirt(message, size = 'Large'):
	"""Prints the size and message of a teeshirt, accepting input"""
	print(f"\nGreat, we will create a {size} tee-shirt for you.")
	print(f"\nIt will have the following message on it:")
	print(f"\n\t{message}")

size_input = input("\nWhat size would you like? Small, Medium or Large? ")
message_input = input("\nWhat should the tee-shirt say on the front? ")

make_shirt(message = 'I love Python!')

make_shirt(size = size_input, message = message_input)