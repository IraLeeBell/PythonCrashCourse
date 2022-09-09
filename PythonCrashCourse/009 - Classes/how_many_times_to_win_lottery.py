from random import choice

powerball_numbers_white = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
powerball_numbers_red = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

my_ticket_white_draw = [choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white)]
my_ticket_red_draw = [choice(powerball_numbers_red)]



print("It's time to draw the winning numbers for this week's PowerBall!")
print("The numbers you picked are as follows:\n")
print(f'\tWhite ball numbers: {my_ticket_white_draw}')
print(f'\tRed ball number: {my_ticket_red_draw}')

print("\nLet's see how many draws it takes for you to get all 5 numbers")
print(f'plus the powerball...')

x = 0
y = 0
z = 0
looping = True

while looping:
	white_draw = [choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white)]
	red_draw = [choice(powerball_numbers_red)]

	if my_ticket_white_draw[0] in white_draw and my_ticket_white_draw[1] in white_draw and my_ticket_white_draw[2] in white_draw and my_ticket_white_draw[3] in white_draw and my_ticket_white_draw[4] in white_draw and my_ticket_red_draw[0] in red_draw:
		print("\nYou have won the lottery!")
		print(f'It took {"{:,}".format(x)} draws for that to happen.')
		print(f'Your numbers of {my_ticket_white_draw} and {my_ticket_red_draw} match the')
		print(f'drawn numbers of {white_draw} and {red_draw}')
		looping = False
	else:
		continue



