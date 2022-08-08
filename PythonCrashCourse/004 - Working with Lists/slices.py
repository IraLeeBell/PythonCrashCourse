pizzas = ['sausage', 'ham', 'cheese', 'meatlovers', 'onion', 'ham and onion', 'no sauce at all just cheese']
print(pizzas)
for pizza in pizzas:
	print(pizza)

print("The first three items in the list are:")
for pizza in pizzas[0:3]:
	print(pizza)

print("The items from the middle of the list are:")
for pizza in pizzas[3:]:
	print(pizza)
print("!")
print("The last three items in the list are:")
for pizza in pizzas[4:7]:
	print(pizza)