# When we use the below we don't need to use dot notation
# from car import Car, ElectricCar

# When we use the below, we have to use dot notation to call the classes (i.t. car.ElectricCar)
import car

my_beetle = car.Car('volkswagon', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'model 3 performance edition', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()