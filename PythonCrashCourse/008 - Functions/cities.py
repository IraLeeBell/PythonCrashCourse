def describe_city(city, country = 'USA'):
	"""Describes a city and its country, with USA as the default"""
	print(f"\n{city.title()} is in {country.title()}.")

describe_city('austin')

describe_city(city = 'new york')

describe_city(city = 'london', country = 'england')