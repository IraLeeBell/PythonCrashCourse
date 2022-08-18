# The import below calls the file pizza_module.py in the same directory
# This time, we're giving the module an alias of "p"


import pizza_module as p

# Since we gave the module an alias of "p", we call it as "p."
# below so that we can access the function "make_pizza()"
# We can simply use "mp()"
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')