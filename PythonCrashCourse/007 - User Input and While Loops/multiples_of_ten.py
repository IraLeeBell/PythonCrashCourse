multiple_of_ten = input("Tell me a number and I'll tell you if it's a multiple of ten. ")
multiple_of_ten = int(multiple_of_ten)

if multiple_of_ten % 10 == 0:
	print(f"The number {multiple_of_ten} is a multple of 10.")
else:
	print(f"The number {multiple_of_ten} is not a multiple of 10.")