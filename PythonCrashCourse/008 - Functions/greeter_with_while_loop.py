def get_formatted_name(first_name, last_name):
	"""returns a full name, neatly formatted"""
	full_name = f"\n{first_name} {last_name}"
	return full_name.title()

# this is an infinite loop!

while True:
	print("\nPlease tell me your name.")
	f_name = input("First name? ")
	l_name = input("Last name? ")

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"Hello, {formatted_name}!")


