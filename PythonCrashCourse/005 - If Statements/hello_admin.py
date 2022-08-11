users = ['john.smith@', 'ringo.star', 'george.washington', 'albert.einstein', 'john.kennedy', 'administrator']
for user in users:
	if user == 'administrator':
		print(f"\nHello, {user.title()}. Would you like to see a status report?")
	else:
		print(f"\nHello, {user}. Thank you for logging in again.")

