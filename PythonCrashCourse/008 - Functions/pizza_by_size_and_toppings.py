# The following takes in positional and arbitrary arguments..

def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make"""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"\n- {topping}")


make_pizza(14, 'pepperoni', 'extra cheese')
make_pizza(16, 'thin crust', 'sausage', 'green peppers')