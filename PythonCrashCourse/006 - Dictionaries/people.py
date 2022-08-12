person_0 = {
		'first': 'john',
		'middle': 'lee',
		'last': 'smith',
		'age': 42,
		'city': 'jacksonville'
		}

person_1 = {
		'first': 'john',
		'middle': 'lee',
		'last': 'smith',
		'age': 42,
		'city': 'jacksonville'
		}

person_2 = {
		'first': 'john',
		'middle': 'lee',
		'last': 'smith',
		'age': 42,
		'city': 'jacksonville'
		}

people = [person_0, person_1, person_2]

for x in people:
	for key, value in x.items():
		print(f"\n{key}: {value}")
