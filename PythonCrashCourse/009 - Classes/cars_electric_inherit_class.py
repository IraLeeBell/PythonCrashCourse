class Car:
	""" A simple attempt to represent a car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		if miles >= self.odometer_reading:
			self.odometer_reading += miles
		else:
			print("You can't roll back an odometer!")

	def fill_gas_tank(self):
		print(f"You have just filled up the gas tank in your {self.year} {self.make} {self.model}!")

class ElectricCar(Car):
	"""Represent aspects of cars, specific to electric vehicles"""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attribute specific to the electric car.
		"""
		super().__init__(make, model, year)
		self.battery_size = 75

	
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size} kWh battery.")

	def fill_gas_tank(self):
		print(f"Electric cars do not need gas, so this isn't necessary!")

my_new_car = Car('mercedes', 'g-wagon', 2023)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

my_tesla = ElectricCar('tesla', 'plaid', '2022')
print(my_tesla.get_descriptive_name())
my_tesla.increment_odometer(42)
my_tesla.read_odometer()
my_tesla.describe_battery()
my_tesla.fill_gas_tank()