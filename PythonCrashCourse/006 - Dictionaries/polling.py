favorite_languages = {
	'ira': 'python',
	'blair': 'english',
	'christian': 'c#',
	'scott': 'java',
	'kale': 'ruby',
	'elinor': 'apple basic'
	}

names = ['ira', 'blair', 'todd', 'casey']

if names:
	for name in names:
		if name in favorite_languages:
			print(f"Thank you for taking the poll, {name.title()}!")
		else:
			print(f"Please take our poll, {name.title()}.")