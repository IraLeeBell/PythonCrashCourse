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