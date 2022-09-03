class Cars:
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


my_new_car = Cars('mercedes', 'g-wagon', 2023)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

# Let's drive 10 miles.

my_new_car.odometer_reading = 10
my_new_car.read_odometer()

# let's drive 10 more miles - so we update to 20, but this time we 
# call the method in the class...

my_new_car.update_odometer(20)
my_new_car.read_odometer()

# but can we do math? sure.. let's get to 30

my_new_car.update_odometer(my_new_car.odometer_reading + 10)
my_new_car.read_odometer()

# Now we try to pull a Ferris Buller..

my_new_car.update_odometer(20)
my_new_car.read_odometer()

# time for a road trip... and calling the increment method
my_new_car.increment_odometer(3000)
my_new_car.read_odometer()