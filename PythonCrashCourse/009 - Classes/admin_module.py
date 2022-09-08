from user_module import Users

class Privileges:
	def get_privileges(self):
		privileges3=['can add post', 'can delete post', 'can ban user']
		return privileges3

class Administrators(Users):
	def __init__(self, first_name, last_name, age, birth_city, allergies):
		super().__init__(first_name, last_name, age, birth_city, allergies)

		self.show_priv = Privileges()