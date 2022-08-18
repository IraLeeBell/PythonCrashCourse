def make_pizza(size, *toppings):
	"""Print the details of the pizza we are about to make"""
	print("\nWe are going to make the following pizza for you!")
	for topping in toppings:
		print(f"\n- {topping}")
