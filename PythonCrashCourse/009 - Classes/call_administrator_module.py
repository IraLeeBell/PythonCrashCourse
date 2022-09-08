from administrator_module import Administrators

mike = Administrators('mike', 'jones', 31, 'destin', 'nothing')

print(f"{mike.first_name.title()} {mike.last_name.title()} has the following privileges: " + str(mike.show_priv.get_privileges3()))

