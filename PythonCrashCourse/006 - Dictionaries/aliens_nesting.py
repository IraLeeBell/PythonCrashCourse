alien_0 = {
	'color': 'green',
	'points': 5
}

alien_1 = {
	'color': 'yellow',
	'points': 10
}

alien_2 = {
	'color': 'red',
	'points': 15
}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

# Now let's use the range function to create 30 green aliens
#
# Make an empty list for storing aliens
aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 'five', 'speed': 'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
	print(alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'

for alien in aliens[:5]:
	print(alien)

# Show how many aliens have been created
print(f"The total number of aliens is {len(aliens)}.")



