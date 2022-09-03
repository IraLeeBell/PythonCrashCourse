class Cars:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()

my_new_car = Cars('mercedes', 'g-wagon', 2023)
print(my_new_car.get_descriptive_name())