prompt = "Welcome to the movie theater. Please tell me your age so I"
prompt += "\ncan tell you the price of the movie! Enter quit when done."
prompt += "\n>>> "

age = ""
active = True

while active:
	age = input(prompt)
	if age == 'quit':
		active = False
	else:
		age = int(age)
		if age <= 3:
			print(f"Since you are {age} years old, the ticket is free!")
		elif age > 3 and age <= 12:
			print(f"since you are {age} years old, the ticket is $10.")
		else:
			print(f"Since you are {age} years old, the ticket is $15.")
