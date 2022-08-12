rivers = {'nile': 'egypt', 'mississippi': 'united states', 'saskatchewan': 'canada'}

for key, value in rivers.items():
	print(f"The {key.title()} runs through {value.title()}.")

for river in rivers.keys():
	print(river.title())

for country in rivers.values():
	print(country.title())