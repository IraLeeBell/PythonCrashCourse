def make_car(manufacturer, model, **kwargs):
	"""Build a dictionary of the car's information"""
	kwargs['company_manufacturer'] = 'manufacturer'
	kwargs['company_model'] = 'model'
	return kwargs

new_car = make_car('honda','accord')
another_new_car = make_car('mercedes','g-wagon',color='black',upgrade_1='AMG',upgrade_2='22 inch wheels',upgrade_3='driver assist')
print(f"\n{new_car}")
print(f"\n{another_new_car}")