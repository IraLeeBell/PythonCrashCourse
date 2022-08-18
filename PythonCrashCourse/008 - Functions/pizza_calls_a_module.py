# The import below calls the file pizza_module.py in the same directory

import pizza_module

# In order to call the function in pizza_module.py that we imported, we
# have to begin the function call with pizza_module...
pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')