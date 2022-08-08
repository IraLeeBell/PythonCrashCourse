players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

# in the below example, we omit the first slice, for which Python will start with the first item in the list

print(players[:4])

# in the below example, we have a situation similar to the above, except that we have omitted the second item..
# thus python starts with the third item in the list and prints the rest

print(players[2:])

# The below code demonstrates how to loop through a slice, we omit the first slice causing Python to start
# with 0, and then it ends at 2 since we've specified 3 as the end of

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
