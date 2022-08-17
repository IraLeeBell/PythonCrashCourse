def describe_pet(pet_name, animal_type = 'dog'):
	"""Prints a pet name that is passed through an argument/parameter"""
	"""but also uses a default value in the function definition"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'dottie')

# Note that the below also works, but probably isn't a best practice

describe_pet('dottie')

# You can replace the animal type if desired, even though it has
# a default value:

describe_pet(pet_name = 'max', animal_type = 'cat')

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name = 'willie')

# A cat named Max.
describe_pet('max', 'cat')
describe_pet(pet_name = 'max', animal_type = 'cat')
describe_pet(animal_type = 'cat', pet_name = 'max')