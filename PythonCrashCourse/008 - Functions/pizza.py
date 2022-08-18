def make_pizza(*toppings):
	"""Italian man with large mustache yells..."""
	print("\nNext customer please!")

	"""Print the list of toppings that have been requested"""
	print(f"\n\nOk, you want the following toppings {toppings}?")

	"""Summarize the pizza we are about to make"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"\nTopping: {topping}")

make_pizza("pepperoni")

make_pizza('mushrooms', 'green peppers', 'extra cheese')