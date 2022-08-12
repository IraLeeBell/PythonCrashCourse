favorite_languages = {
	'jen': 'python',
	'sara': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

language = favorite_languages['sara'].upper()
print(f"Sara's favorite language is {language}.")


# Now let's loop through the list

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")

# Now let's loop through and just print the names

for name in favorite_languages:
	print(name.title())

# You can also add the .keys() to favorite_languages, with the same results

for name in favorite_languages.keys():
	print(name.title())

# Print something based upon the dictionary matching items in a list..

friends = ['phil', 'sara']
for name in favorite_languages.keys():
	print(f"Hi {name.title()}!")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

# Let's figure out if someone is in the list..

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

# Loop through the dictionary using sorted, then print out something if individuals are in the dictionary

for name in sorted(favorite_languages.keys()):
	print(f"\n{name.title()}, thank you for taking the poll!")
	print(f"I see you like {favorite_languages[name].title()}!")

# Looping through all values in a dictionary

print("\nThe following languages have been mentioned.")
for language in favorite_languages.values():
	print(f"{language.title()}")