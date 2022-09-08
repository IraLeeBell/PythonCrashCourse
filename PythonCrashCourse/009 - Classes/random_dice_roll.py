from random import randint

class Die:
	def __init__(self, sides=20):
		self.sides = sides

	def roll_die(self):
		dice_low_number = 1
		dice_high_number = self.sides
		dice_number = randint(dice_low_number, dice_high_number)
		print(f'\tThe dice has been rolled, resulting in a {dice_number}\n')

	def roll_ten_times(self):
		x = 1
		while x < 11:
			print(f'Roll number {x}:')
			self.roll_die()
			x += 1

lets_play = Die()
lets_play.roll_ten_times()

