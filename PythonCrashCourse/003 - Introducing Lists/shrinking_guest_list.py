# This exercise states that you can invite any three people to dinner, living or dead.
# So who would they be? Use lists to store the people and then print their names. 

dinner_guests = ['stephen hawking', 'issac newton', 'thomas edison', 'benjamin franklin']
print(dinner_guests)
print("\n")

# looks like we have too many guests... I guess we need to remove one
no_room = dinner_guests[1]
dinner_guests.remove(no_room)
print(f"Unfortunately, we didn't have room for {no_room.title()}, so he had to be removed from the guest list.")
print("\n")
print(dinner_guests)
print("\n")

# Now we invite each of them to dinner. 
print(f"Hello, {dinner_guests[0].title()}, would you care to join me for dinner this evening?")
print(f"Hello, {dinner_guests[1].title()}, would you care to join me for dinner this evening?")
print(f"Hello, {dinner_guests[-1].title()}, would you care to join me for dinner this evening?")

# It turns out that one of the guests can't make it.
print("\n")
print(f"Unfortunately, {dinner_guests[-1].title()} won't be able to join me for dinner.")
print(f"We should invite someone else, then. How about {no_room.title()}?")

# Time to replace Ben with Issac in the list
we_now_have_room = no_room
dinner_guests[-1] = we_now_have_room
print(dinner_guests)
print("\n")
print(f"Hello, {dinner_guests[2].title()}, it turns out that we have space available.")
print(f"Would you care to join myself, {dinner_guests[0].title()} and {dinner_guests[1].title()} for dinner this evening?")

# We found a bigger table, so we can invite three more guests. 
# We will add them to the list, using insert and append

print("\n")
print(dinner_guests)
dinner_guests.insert(0, 'neil armstrong')
dinner_guests.insert(2, 'aristotle')
dinner_guests.append('rosa parks')
print(dinner_guests)
print("\n")
print(f"Hello, {dinner_guests[0].title()}, would you care to join me for dinner this evening?")
print(f"Hello, {dinner_guests[2].title()}, would you care to join me for dinner this evening?")
print(f"Hello, {dinner_guests[5].title()}, would you care to join me for dinner this evening?")

# Due to supply chain issues, our new table won't arrive in time
# We now only have room for two guests
print("\n")
sad_message = "Sadly our new table won't arrive in time so I am only able to invite two guests."
print(sad_message)

first_cancellation = dinner_guests.pop()
print(f"I'm sorry, {first_cancellation.title()}, but we are out of room this evening so I need to cancel your invitation.")
print(dinner_guests)
second_cancellation = dinner_guests.pop()
print(f"I'm sorry, {second_cancellation.title()}, but we are out of room this evening so I need to cancel your invitation.")
print(dinner_guests)
third_cancellation = dinner_guests.pop()
print(f"I'm sorry, {third_cancellation.title()}, but we are out of room this evening so I need to cancel your invitation.")
print(dinner_guests)
fourth_cancellation = dinner_guests.pop()
print(f"I'm sorry, {fourth_cancellation.title()}, but we are out of room this evening so I need to cancel your invitation.")
print(dinner_guests)

print("\n")
print(f"Hello, {dinner_guests[0].title()} and {dinner_guests[1].title()}, I am confirming your reservation for dinner this evening.")

# Now to clear the last two items from the list per the exercise
del dinner_guests[1]
del dinner_guests[0]
print(dinner_guests)

# Out of curiosity, can we delete the two remaining list items in one del statement?
# We can do so by using 'list slicing' whereby we state the first index value and then the last value + 1
dinner_guests = ['neil armstrong', 'stephen hawking']
print(dinner_guests)
del dinner_guests[0:2]
print(dinner_guests)