cities = {
	'ocala': {
		'country': 'united states',
		'population': '100,000',
		'fact': 'this is generally where I grew up'
	},

	'gainesville': {
		'country': 'united states',
		'population': '80,000',
		'fact': 'home of the florida gators'
	},

	'tokyo': {
		'country': 'japan',
		'population': '10,000,000',
		'fact': 'great sushi'
	}
}

for key,values in cities.items():
	print(f"\nThis is the information we have on {key.title()}:")
	for x, y in values.items():
		print(f"\t{x.title()}: {y.title()}")