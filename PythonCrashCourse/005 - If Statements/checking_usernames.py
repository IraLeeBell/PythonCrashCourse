current_users = ['john.smith', 'ringo.star', 'george.washington', 'Ira.Bell', 'Albert.Einstein', 'john.kennedy', 'administrator', 'admin']
new_users = ['ringo.star', 'neil.armstrong', 'ira.bell', 'admin', 'aristotle', 'albert.einstein', 'administrator']

current_users_lowercase = [x.lower() for x in current_users]

if new_users:
	for new_user in new_users:
		if new_user in current_users_lowercase and (new_user == 'administrator' or new_user == 'admin'):
			print('\nThat is a reserved user name, please try again.')
		elif new_user in current_users_lowercase:
			print(f"\nThe user name {new_user} has already been taken.")
			print("Please choose a new user name.")
		else:
			print(f"\nThe user name {new_user} is available.")

