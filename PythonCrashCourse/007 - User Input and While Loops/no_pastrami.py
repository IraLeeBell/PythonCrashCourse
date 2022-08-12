sandwich_orders = ['pastrami', 'burger', 'grilled cheese', 'pastrami', 'ham sandwich', 'turkey club', 'pastrami']
finished_sandwiches = []

print("Unfortunately the deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')


while sandwich_orders:
	finished = sandwich_orders.pop()

	print(f"The order for the {finished} is complete")
	finished_sandwiches.append(finished)

print("\nThe following sandwiches were created.")
for sandwiches in finished_sandwiches:
	print(f"\t{sandwiches.title()}")