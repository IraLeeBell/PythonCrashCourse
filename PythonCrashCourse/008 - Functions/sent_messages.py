def show_text_messages(text_list):
	print("\nThe following are the text messages in the list.")
	for text in text_list:
		print(f"\n{text}")

def send_text_messages(text_list, sent_list):
	print("\nThe following messages were sent.")
	while text_list:
		sent = text_list.pop()
		print(f"\n{sent}")
		sent_list.append(sent)

text_list = ["Hey, how is your day going?", "Calvin, any updates on the concrete slab?", "Man, it sure is hot in Florida this week."]
sent_list = []

# Display the messages contained in text_list

show_text_messages(text_list)

# Move the messages from text_list to sent_list, printing each

send_text_messages(text_list, sent_list)

#Now to prove that text_list was emptied

print(text_list)