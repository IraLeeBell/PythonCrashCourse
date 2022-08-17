def build_person(first_name, last_name):
	"""Returns a dictionary of information about a person""" 
	person = {'first': first_name, 'last': last_name}
	return person

musican = build_person('jimi', 'hendrix')
print(musican)