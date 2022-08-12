number_in_party = input("How many people will be dining with us this evening? ")
number_in_party = int(number_in_party)

if number_in_party > 8:
	print(f"Because you have more than {number_in_party} people,")
	print(f"you will need to wait for a table.")
else:
	print(f"Excellent, your table is ready now.")