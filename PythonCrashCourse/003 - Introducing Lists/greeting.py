friends = ['blair', 'todd', 'randy', 'casey', 'ryan']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])

print("\n")

print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())
print(friends[4].title())

print("\n")

# This time I used a -1 for the last item in the array, which designates the same as if I had used 4
message = f"My list of friends is {friends[0].title()}, {friends[1].title()}, {friends[2].title()}, {friends[3].title()}, and {friends[-1].title()}."

print(message)

hello_blair = f"Hello, {friends[0].title()}! How was your day?"
hello_todd = f"Hello, {friends[1].title()}! How was your day?"
hello_randy = f"Hello, {friends[2].title()}! How was your day?"
hello_casey = f"Hello, {friends[3].title()}! How was your day?"
hello_ryan = f"Hello, {friends[4].title()}! How was your day?"

print("\n")

print(hello_blair)
print(hello_todd)
print(hello_randy)
print(hello_casey)
print(hello_ryan)
