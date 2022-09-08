from random import choice

powerball_numbers_white = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
powerball_numbers_red = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

white_draw = [choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white)]
red_draw = [choice(powerball_numbers_red)]

my_ticket_white_draw = [choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white), choice(powerball_numbers_white)]
my_ticket_red_draw = [choice(powerball_numbers_red)]

print("It's time to draw the winning numbers for this week's PowerBall!")
print("The numbers you picked are as follows:\n")
print(f'\tWhite ball numbers: {my_ticket_white_draw}')
print(f'\tRed ball number: {my_ticket_red_draw}')

print("\nThis week's winning numbers are as follows:")
print(f'\tWhite ball numbers: {white_draw}')
print(f'\tRed ball numbers: {red_draw}')

print(".\n..checking to see if your numbers match...")

x = 0
y = 0
z = 0

# Check white ball # 1
if my_ticket_white_draw[0] in white_draw:
	print(f"We have a match! {my_ticket_white_draw[0]} is a winning white ball number!")
	x += 1
else:
	print(f"....{my_ticket_white_draw[0]} is not a winning white ball number.")

# Check white ball # 2
if my_ticket_white_draw[1] in white_draw:
	print(f"We have a match! {my_ticket_white_draw[1]} is a winning white ball number!")
	x += 1
else:
	print(f"....{my_ticket_white_draw[1]} is not a winning white ball number.")

# Check white ball # 3
if my_ticket_white_draw[2] in white_draw:
	print(f"We have a match! {my_ticket_white_draw[2]} is a winning white ball number!")
	x += 1
else:
	print(f"....{my_ticket_white_draw[2]} is not a winning white ball number.")

# Check white ball # 4
if my_ticket_white_draw[3] in white_draw:
	print(f"We have a match! {my_ticket_white_draw[3]} is a winning white ball number!")
	x += 1
else:
	print(f"....{my_ticket_white_draw[3]} is not a winning white ball number.")

# Check white ball # 5
if my_ticket_white_draw[4] in white_draw:
	print(f"We have a match! {my_ticket_white_draw[4]} is a winning white ball number!")
	x += 1
else:
	print(f"....{my_ticket_white_draw[4]} is not a winning white ball number.")

# Check red ball
if my_ticket_red_draw[0] in red_draw:
	print(f"We have a match! {my_ticket_white_draw[0]} is a winning red ball number!")
	x += 1
else:
	print(f"....{my_ticket_red_draw[0]} is not a winning red ball number.")

