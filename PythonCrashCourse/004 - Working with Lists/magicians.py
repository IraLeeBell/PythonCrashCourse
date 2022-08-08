magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}!\n")
print("Thank you everyone, that was a great magic show!")

# In the below code, we fail to indent the second line in the loop, which causes it to execute outside of the loop's completion
# As a result, line 17 only prints for the last item stored to the magician variable/container, which is carolina

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}!\n")

# In the below code, we accidentally indent the "Thank You..." line, which causes it to be included in the loop...

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}!\n")

	print("Thank you everyone, that was a great magic show!")

