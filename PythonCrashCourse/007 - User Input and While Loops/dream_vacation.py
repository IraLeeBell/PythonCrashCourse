responses = {}
polling_active = True


while polling_active:
	name = input("What is your name? ")
	place = input("Where would your dream vacation be? ")

	responses[name] = place

	repeat = input("Would you like another person to answer? yes/no ")
	if repeat == 'no':
		polling_active = False

print("\n-=-=- Polling Results -=-=-")
for name, place in responses.items():
	print(f"{name.title()} would like to go to {place.title()}.")
