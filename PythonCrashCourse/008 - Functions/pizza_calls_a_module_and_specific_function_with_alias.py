# The import below calls the file pizza_module.py in the same directory
# However, it only imports the specific make_pizza function and nothing else
# that might be contained in the file..

# The difference here is that we're giving the function the alias "mp"
# So we can call it as such below...

from pizza_module import make_pizza as mp

# This time, we don't need to call the function with "pizza_module."
# We can simply use "mp()"
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')