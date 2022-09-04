class Users:
	def __init__(self, first_name, last_name, age, birth_city, allergies):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.birth_city = birth_city
		self.allergies = allergies

	def describe_user(self):
		print(f'{self.first_name.title()} {self.last_name.title()} is a {self.age} year old from {self.birth_city.title()} who is allergic to {self.allergies}.')



	def greet_user(self):
		print(f'Hi, {self.first_name.title()} {self.last_name.title()}! You are looking rather young, for a {self.age} year old!')

class Administrators(Users):
	def __init__(self, first_name, last_name, age, birth_city, allergies):
		super().__init__(first_name, last_name, age, birth_city, allergies)

	def get_privileges(self):
		
		privileges=['can add post', 'can delete post', 'can ban user']
		print(f"{self.first_name.title()} {self.last_name.title()} has the following privileges: {privileges}")

	def get_privileges2(self):
		privileges2=['can add post', 'can delete post', 'can ban user']
		return privileges2



carl = Users('carl', 'smith', 51, 'austin', 'sulfa')
paul = Users('paul', 'george', 23, 'dallas', 'peanuts')
wanda = Users('wanda', 'mckay', 45, 'new york city', 'nothing')
mike = Administrators('mike', 'jones', 31, 'destin', 'nothing')


carl.describe_user()
carl.greet_user()
print("\n")
paul.describe_user()
paul.greet_user()
print("\n")
wanda.describe_user()
wanda.greet_user()
print("\n")
mike.get_privileges()
print("\n")
print(f"{mike.first_name.title()} {mike.last_name.title()} has the following privileges: " + str(mike.get_privileges2()))

