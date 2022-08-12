# This code is really neat, as we store lists in a dictionary, for some but
# not all of the key/value pairs. Then, we iterate through the dictionary to
# output the multiple values (as lists) when the program locates such

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sara': 'c',
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")