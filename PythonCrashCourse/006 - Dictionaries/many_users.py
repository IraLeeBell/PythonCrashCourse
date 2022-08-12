# This example is neat because there is a dictionary within a dictionary. 
# Things that I noted... we need a comma after the value of each key (the
# value itself is a dictionary. Also this is the first time in the text
# that we are using the f"" function outside of a print command...

users = {
	
	'ibell': {
		'first': 'ira',
		'last': 'bell',
		'location': 'nashville'
		},

	'jsmith': {
		'first': 'john',
		'last': 'smith',
		'location': 'nashville'
	}
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = f"{user_info['location']}"

	print(f"\tFull Name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")