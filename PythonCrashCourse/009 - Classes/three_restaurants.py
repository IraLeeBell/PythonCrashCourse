class Restaurant:
	def __init__(self,restaurant_name, describe_restaurant):
		self.restaurant_name = restaurant_name
		self.describe_restaurant = describe_restaurant

	def open_restaurant(self):
		print(f"{self.restaurant_name}, the {self.describe_restaurant} restaurant is now open.")

	def close_restaurant(self):
		print(f"{self.restaurant_name}, the {self.describe_restaurant} restaurant is now closed.")

	def restaurant_ad(self):
		print(f"We are the best {self.describe_restaurant} restaurant in the mall!")


mall_food_1 = Restaurant("Mario's Pizza Pie Shop", "Italian")
mall_food_2 = Restaurant("World Famous Cookies", "Dessert")
mall_food_3 = Restaurant("Fruits and Veggies", "Smoothie")

mall_food_1.open_restaurant()
mall_food_2.open_restaurant()
mall_food_3.open_restaurant()

mall_food_1.restaurant_ad()
mall_food_2.restaurant_ad()
mall_food_3.restaurant_ad()

mall_food_1.close_restaurant()
mall_food_2.close_restaurant()
mall_food_3.close_restaurant()