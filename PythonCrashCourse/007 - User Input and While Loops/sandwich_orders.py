sandwich_orders = ['burger', 'grilled cheese', 'ham sandwich', 'turkey club']
finished_sandwiches = []

while sandwich_orders:
	finished = sandwich_orders.pop()

	print(f"The order for the {finished} is complete")
	finished_sandwiches.append(finished)

print("\nThe following sandwiches were created.")
for sandwiches in finished_sandwiches:
	print(f"\t{sandwiches.title()}")