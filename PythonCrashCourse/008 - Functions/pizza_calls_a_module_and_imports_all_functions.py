# The import below calls the file pizza_module.py in the same directory
# This time, we use an asterik to import all functions

# This is bad practice... because altough it allows us to avoid using the
# "pizza_module." format to access a given function, it could end up conflicting
# with the program code and break something 

from pizza_module import *

# Nontheless, shown below is our ability to access the function "make_pizza()"
# without the "pizza_module." notation..

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')