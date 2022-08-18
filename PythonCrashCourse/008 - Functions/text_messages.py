def show_text_messages(text_list):
	print("\nThe following are the text messages in the list.")
	for text in text_list:
		print(f"\n{text}")

text_list = ["Hey, how is your day going?", "Calvin, any updates on the concrete slab?", "Man, it sure is hot in Florida this week."]

show_text_messages(text_list)