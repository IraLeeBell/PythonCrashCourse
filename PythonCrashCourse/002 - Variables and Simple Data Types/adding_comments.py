# Adding first and last name in lowercase, so that we can manipulate themn with the title() method later
first_name = "issac"
last_name = "asimov"

# Adding the first and last name in lowercase to a new variable called full_name
full_name = f"{first_name} {last_name}"

# Adding the full_name variable to the full_name_proper variable, using the title() method
# to capitalize the first letters of each name
full_name_proper = f"{full_name.title()}"

# Instead of adding the full quote in to one variable, I have created three variables to demonstrate 
# the use of adding strings together with seperate new line \n and tab \u use
quote = "\n\tYour assumptions are your windows on the world."
quote_cont = "\n\tScrub them off every once in a while,"
quote_cont_further = "\n\tor the light won't come in."
full_quote = f"{quote} {quote_cont} {quote_cont_further}"

# Now we store the whole sentence required for the exercise in the message variable and print it
message = f"\n\t{full_name_proper} once said, {full_quote}"
print(message)