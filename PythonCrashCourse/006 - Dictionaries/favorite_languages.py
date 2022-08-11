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