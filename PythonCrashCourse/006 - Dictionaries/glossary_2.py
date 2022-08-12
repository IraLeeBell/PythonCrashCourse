glossary = {
	'Python': 'A programming language that is highly readable and functional',
	'List': 'A way to store several object in python which you can iterate through and read, etc.',
	'Integer': 'A number, such as 1 or 9.',
	'Boolean Value': 'True or False',
	'Is Equal To?': 'The operator ==, when used, can evaluate whether two things are equal to each other.',
	'Set': 'A type of list that uses braces but no key value pair, and is not in any specific order.',
	'Dictionary': 'A way to store items as key value pairs.',
	'Sublime Text': 'A developer friendly rich text-editor.',

	}

print("The following are some things that I've learned about Python:")

# We can comment the below section out, because we now know
# how to loop through dictionaries
# print("\n")
# print("\nPython:\n" + glossary['Python'])
# print("\nList:\n" + glossary['List'])
# print("\nInteger:\n" + glossary['Integer'])
# print("\nBoolean Value:\n" + glossary['Boolean Value'])
# print("\nIs Equal To?:\n" + glossary['Is Equal To?'])

for key, value in glossary.items():
	print(f"\n{key}: {value}")