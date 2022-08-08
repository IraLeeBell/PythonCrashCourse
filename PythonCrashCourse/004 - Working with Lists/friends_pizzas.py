pizzas = ['sausage', 'ham', 'cheese', 'meatlovers', 'onion', 'ham and onion', 'no sauce at all just cheese']


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

# Creating a list called friend pizzas which copies the original list
friend_pizzas = pizzas[:]
pizzas.append("white slice")
friend_pizzas.append("mushroom")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("\n")

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
print("\n")
print(pizzas)
print(friend_pizzas)