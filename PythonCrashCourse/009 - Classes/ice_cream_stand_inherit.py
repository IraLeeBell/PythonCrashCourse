class Restaurant:
	def __init__(self,restaurant_name, describe_restaurant):
		self.restaurant_name = restaurant_name
		self.describe_restaurant = describe_restaurant

	def open_restaurant(self):
		print(f"{self.restaurant_name}, the {self.describe_restaurant} restaurant is now open.")

	def close_restaurant(self):
		print(f"{self.restaurant_name}, the {self.describe_restaurant} restaurant is now closed.")

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, describe_restaurant):
		super().__init__(restaurant_name, describe_restaurant)
		self.flav1 = "chocolate"
		self.flav2 = "vanilla"
		self.flav3 = "strawberry"

	def describe_flavors(self):
		print(f"{self.restaurant_name}, the {self.describe_restaurant} restaurant, will make you an ice cream cone with the following flavors: {self.flav1}, {self.flav2}, and {self.flav3}")


mall_food = Restaurant("Mario's Pizza Pie Shop", "Italian")
mall_food.open_restaurant()
print("\n")
mall_food.close_restaurant()
print("\n")
sweet_treat = IceCreamStand('Lickity Splits', 'dessert')
sweet_treat.open_restaurant()
print("\n")
sweet_treat.describe_flavors()
print("\n")
sweet_treat.close_restaurant()


