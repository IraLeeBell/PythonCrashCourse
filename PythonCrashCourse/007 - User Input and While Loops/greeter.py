name = input("Please enter your name: ")
print(f"Hello, {name.title()}!")

# more 

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name.title()}!")

# The below works, but it is treated as a string instead of an integer
age = input("How old are you? ")
print(age)