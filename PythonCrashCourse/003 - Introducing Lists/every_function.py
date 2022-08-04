# The exercise calls for me to think about things that I could store in a list. Then,
# try to use all of the things that were discussed in this chapter. 

# Create two lists
pets = ['dottie', 'maple', 'kitty', 'max']
family = ['elinor', 'blair', 'scott', 'christian', 'kale']
holidays = ['christmas', 'thanksgiving', 'new year\'s eve']

# Let's view the data as lists
print("\nHere is the list of pets:")
print(pets)
print("\nHere is the list of family members:")
print(family)
print("\nHere is the list of holidays:")
print(holidays)

# Let's output the data from the lists in sentences
print(f"\nThe list of pets is as follows: {pets[0].title()}, {pets[1].title()}, {pets[2].title()} and {pets[3].title()}.")
print(f"\nThe list of family is as follows: {family[0].title()}, {family[1].title()}, {family[2].title()}, {family[3].title()} and {family[4].title()}.")
print(f"\nThe list of holidays is as follows: {holidays[0].title()}, {holidays[1].title()} and {holidays[2].title()}.")

# Let's temporarily sort each list and prove that the sort didn't affect the list permanantely
print("\nHere is the temporarily sorted pets list:")
print(sorted(pets))
print("\nHere is the originally sorted pets list:")
print(pets)
print("\nHere is the temporarily sorted family list:")
print(sorted(family))
print("\nHere is the originally sorted pets list:")
print(family)
print("\nHere is the temporarily sorted holiday list:")
print(sorted(holidays))
print("\nHere is the originally sorted pets list:")
print(holidays)

# We'll do the same exercise, temporarily, but in reverse
print("\nHere is the temporarily sorted pets list:")
print(sorted(pets, reverse=True))
print("\nHere is the originally sorted pets list:")
print(pets)
print("\nHere is the temporarily sorted family list:")
print(sorted(family, reverse=True))
print("\nHere is the originally sorted pets list:")
print(family)
print("\nHere is the temporarily sorted holiday list:")
print(sorted(holidays, reverse=True))
print("\nHere is the originally sorted pets list:")
print(holidays)

# Let's add an item to each list and print each list
pets.append('scooby')
family.append('guy on the couch')
holidays.append('mars day')

print("\nHere is the list of pets:")
print(pets)
print("\nHere is the list of family members:")
print(family)
print("\nHere is the list of holidays:")
print(holidays)

# Let's permanantley sort the lists
pets.sort()
print("\nHere is the sorted list of pets:")
print(pets)
family.sort()
print("\nHere is the sorted list of family members:")
print(family)
holidays.sort()
print("\nHere is the sorted list of holidays:")
print(holidays)

# Let's permanately reverse the sort of the lists
pets.sort(reverse = True)
print("\nHere is the reverse sorted list of pets:")
print(pets)
family.sort(reverse = True)
print("\nHere is the reverse sorted list of family members:")
print(family)
holidays.sort(reverse = True)
print("\nHere is the revserse sorted list of holidays:")
print(holidays)

# We have some bad data in the pets list, let's del the bad data
print(pets)
print(f"\nWho the heck is {pets[0].title()}? Let's remove this one.")
del pets[0]
print(f"\nMuch better to see the accurate list of pets: {pets[0].title()}, {pets[1].title()}, {pets[2].title()} and {pets[3].title()}.")

# We have some bad data in the family list, let's remove the bad data
print(family)
print(f"\nWho the heck is {family[2].title()}? Let's remove this one.")
so_weird = family[2]
family.remove(so_weird)
print(f"\nMuch better to see the accurate list of family: {family[0].title()}, {family[1].title()}, {family[2].title()}, {family[3].title()} and {family[4].title()}.")

# We have some bad data in the family list, let's pop the bad data
print(holidays)
holidays.append(holidays[2])
print(holidays)
del holidays[2]
print(holidays)
this_is_earth_dude = holidays.pop()
print(f"\nI have no idea where the {this_is_earth_dude.title()} holiday came from. I swear I\'m not a space cadet.")
print(f"\nThe accurate list of holidays is {holidays[0].title()}, {holidays[1].title()} and {holidays[2].title()}")

# Not sure if I missed anything covered in the chapter, but if so - please let me know and I'll update. 







