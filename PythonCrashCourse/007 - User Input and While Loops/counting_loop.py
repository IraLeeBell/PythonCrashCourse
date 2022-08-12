current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 3 == 0:
		continue

	print(current_number)
# The above line is only executed when the above if statement is
# not true. In this case, since 3/3 = no remainder (thus zero), 3
# isn't printed in the output. The same is true for 9. We "continue"
# back to the top of the loop instead, as lont as the current_number
# variable is less than 10 with the last test.