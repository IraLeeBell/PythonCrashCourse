# The import below calls the file pizza_module.py in the same directory
# However, it only imports the specific make_pizza function and nothing else
# that might be contained in the file..

from pizza_module import make_pizza

# This time, we don't need to call the function with "pizza_module."
# We can simply use "make_pizza()"
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')