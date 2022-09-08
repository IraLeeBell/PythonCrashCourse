from admin_module import Administrators

mike = Administrators('mike', 'jones', 23, 'Washington', 'peanuts')
print(f'{mike.first_name.title()} {mike.last_name.title()} from {mike.birth_city.title()} has the following privileges: \n' + str(mike.show_priv.get_privileges()))