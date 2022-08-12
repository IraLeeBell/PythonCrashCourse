favorite_places = {
	'ira': ['bahamas', 'florida', 'nashville'],
	'blair': ['destin', 'nashville', 'hawaii'],
	'elinor': ['home'],
	'scott': ['colorado', 'viginia']
}

for name, places in favorite_places.items():
	print(f"\n{name.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}")