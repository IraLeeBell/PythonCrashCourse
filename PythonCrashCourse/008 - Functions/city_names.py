def city_country(city, country):
	"""returns a city and country, nicely formatted"""
	result = f"{city}, {country}"
	print(result.title())

city_country('new york', 'united states')
city_country('london', 'england')
city_country('barcelona', 'spain')