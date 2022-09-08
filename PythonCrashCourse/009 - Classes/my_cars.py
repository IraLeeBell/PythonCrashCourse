# When we use the below we don't need to use dot notation
# from car import Car, ElectricCar

# When we use the below, we have to use dot notation to call the classes (i.t. car.ElectricCar)
# import car

# When we use the below we don't need to use dot notation
# This approach is not recommended since it's unclear which classes you're
# using from a given module, but it does work. 
# from car import *

# We can also use aliases, like shown below
from car import Car as C, ElectricCar as EC

my_beetle = C('volkswagon', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'model 3 performance edition', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()