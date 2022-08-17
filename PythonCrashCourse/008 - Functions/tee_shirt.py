def tee_shirt(size, message):
	"""Prints the size and message to be displayed on a tee shirt"""
	print(f"\nGreat, we will create a {size} tee-shirt for you.")
	print(f"\nIt will have the following message on the front:")
	print(f"\t{message}")

sizeinput = input("\nWhat size tee-shirt do you need? Large, Medium or Small? ")
messageinput = input("\nWhat would you like the tee shirt message to be? ")

tee_shirt(sizeinput, messageinput)