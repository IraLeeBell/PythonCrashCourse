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