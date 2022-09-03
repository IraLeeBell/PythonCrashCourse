class Restaurant:
	def __init__(self,restaurant_name, describe_restaurant):
		self.restaurant_name = restaurant_name
		self.describe_restaurant = describe_restaurant

	def open_restaurant(self):
		print(f"{self.restaurant_name}, the {self.describe_restaurant} restaurant is now open.")

	def close_restaurant(self):
		print(f"{self.restaurant_name}, the {self.describe_restaurant} restaurant is now closed.")
"Mario's Pizza Pie Shop"


mall_food = Restaurant("Mario's Pizza Pie Shop", "Italian")



mall_food.open_restaurant()
mall_food.close_restaurant()