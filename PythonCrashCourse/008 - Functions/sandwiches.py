def make_sandwich(*ingredients):
	"""Print a list showing the details of the sandwich we are about to make"""
	print("\nWe are about to make the following sandwich:")
	for ingredient in ingredients:
		print(f"\n- {ingredient}")


make_sandwich('plain')

make_sandwich('turkey', 'cheese')

make_sandwich('swiss cheese', 'cheddar cheese', 'american cheese')