first_name = " ira"
middle_name = " lee "
last_name = "bell "
full_name_unformatted = f"{first_name} {middle_name} {last_name}"
print(full_name_unformatted)

full_name_formatted = f"{first_name.lstrip()} {middle_name.strip()} {last_name.rstrip()}"
print(full_name_formatted)

first_name_formatted = f"\n\t{first_name.lstrip()}"
middle_name_formatted = f"\n\t{middle_name.strip()}"
last_name_formatted = f"\n\t{last_name.rstrip()}"
print(first_name_formatted)
print(middle_name_formatted)
print(last_name_formatted)
