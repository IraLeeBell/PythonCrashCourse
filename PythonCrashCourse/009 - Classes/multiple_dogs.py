class Dog:
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name age and attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")


my_dog = Dog('Maple', 10)
your_dog = Dog('Dottie', 2)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()