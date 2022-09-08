from random import choice

powerball_numbers_white = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
powerball_numbers_red = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

white_draw_1 = choice(powerball_numbers_white)
white_draw_2 = choice(powerball_numbers_white)
white_draw_3 = choice(powerball_numbers_white)
white_draw_4 = choice(powerball_numbers_white)
white_draw_5 = choice(powerball_numbers_white)
red_draw = choice(powerball_numbers_red)

print("It's time to draw the winning numbers for this week's PowerBall!")
print("\nThe winning numbers are...")
print(f'{white_draw_1} {white_draw_2} {white_draw_3} {white_draw_4} {white_draw_5}')
print("\nAnd the red powerball number is...")
print(red_draw)