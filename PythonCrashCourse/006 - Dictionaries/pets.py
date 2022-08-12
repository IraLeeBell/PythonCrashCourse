pet_0 = {
	'name': 'dottie',
	'owner': 'blair',
	'type': 'dog'
}

pet_1 = {
	'name': 'kitty',
	'owner': 'elinor',
	'type': 'cat'
}

pet_2 = {
	'name': 'max',
	'owner': 'elinor',
	'type': 'cat'
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
	for key, value in pet.items():
		print(f"{key}: {value}")