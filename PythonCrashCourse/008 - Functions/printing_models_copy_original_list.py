def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

def show_unprinted_models(unprinted_designs):
	print("\nThese are the items in the unprinted list which was copied, not emptied:")
	for unprinted_design in unprinted_designs:
		print(unprinted_design)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
show_unprinted_models(unprinted_designs)



