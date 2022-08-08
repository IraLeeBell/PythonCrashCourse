my_foods = ['pizza', 'flafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Now to do it with a for loop...

for my_food in my_foods:
	print(my_food)
print("\n")

for friend_food in friend_foods:
	print(friend_food)
print("\n")