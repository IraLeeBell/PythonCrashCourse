class Cat:
	def __init__(self,name,age):
		self.name = name
		self.age = age


	def sit(self):
		print(f'{self.name} is now sitting.')

	def rollover(self):
		print(f'{self.name} is now rolling over.')

my_cat = Cat('Freckles', 5)

print(f"My cat's name is {my_cat.name}")
print(f"My cat is {my_cat.age} years old.")

my_cat.rollover()

my_cat.sit()