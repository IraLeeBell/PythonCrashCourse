users = ['john.smith', 'ringo.star', 'george.washington', 'albert.einstein', 'john.kennedy', 'administrator']
for user in users:
	if user == 'administrator':
		print(f"\nHello, {user.title()}. Would you like to see a status report?")
	else:
		print(f"\nHello, {user}. Thank you for logging in again.")

# Add a test to ensure that the list of users is not empty...

users = []
if users:
	for user in users:
		if user == 'administrator':
			print(f"\nHello, {user.title()}. Would you like to see a status report?")
		else:
			print(f"\nHello, {user}. Thank you for logging in again.")
else:
	print("We need to find some users!")
