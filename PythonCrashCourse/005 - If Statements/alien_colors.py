alien_color = 'green'
if alien_color == 'green':
    points = 5
    print(f"\nYou have been assigned {points} points.")
else:
    points = 0
    print(f"\nYou have been assigned {points} points.")

# Do the same exercise again, but this time it should fail and produce no output

alien_color = 'red'
if alien_color == 'green':
    points = 5
    print(f"\nYou have been assigned {points} points.")
else:
    points = 0