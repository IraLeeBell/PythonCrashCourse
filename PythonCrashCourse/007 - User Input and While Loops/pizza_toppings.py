toppings = "What would you like on your pizza?"
toppings += "\nEnter quit to end. "

active = True

while active:
	x = input(toppings)
	if x == 'quit':
		active = False
	else:
		print(f"I will add {x} to your pizza.")