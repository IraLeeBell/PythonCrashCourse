# I added some numbers to this loop, so I could observe where the
# dictionary is actually created, etc. 

responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	print("1")
	response = input("Which mountain would you like to climb someday? ")
	print("2")

	# Store the response in the dictionary.
	responses[name] = response
	print("3")

	# Find out if anyone else is going to take the poll. 
	repeat = input("Would you like to let another person respond? (yes/no) ")
	print("4")
	if repeat == 'no':
		print("5")
		polling_active = False

# Polling is complete, show the results
print("6")
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")